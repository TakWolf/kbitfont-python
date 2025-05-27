from __future__ import annotations

from io import BytesIO
from os import PathLike
from typing import Any, BinaryIO

from lxml import etree

from kbitfont.error import KbitsError, KbitxError
from kbitfont.glyph import KbitGlyph
from kbitfont.names import KbitNames
from kbitfont.props import KbitProps
from kbitfont.utils import kbits, kbitx, base64
from kbitfont.utils.stream import Stream


def _kern_pairs_key_comparator(item: tuple[tuple[int | str, int | str], int]) -> tuple[int, int | None, str | None, int, int | None, str | None]:
    left, right = item[0]
    if isinstance(left, int):
        left_type = 0
        left_int_key = left
        left_str_key = None
    else:
        left_type = 1
        left_int_key = None
        left_str_key = left
    if isinstance(right, int):
        right_type = 0
        right_int_key = right
        right_str_key = None
    else:
        right_type = 1
        right_int_key = None
        right_str_key = right
    return left_type, left_int_key, left_str_key, right_type, right_int_key, right_str_key


class KbitFont:
    @staticmethod
    def parse_kbits(stream: bytes | bytearray | BinaryIO) -> KbitFont:
        if isinstance(stream, (bytes, bytearray)):
            stream = BytesIO(stream)
        stream = Stream(stream)

        if stream.read(8) != kbits.MAGIC_NUMBER:
            raise KbitsError('bad magic number')
        if stream.read_uint32() != kbits.SPEC_VERSION:
            raise KbitsError('bad spec version')

        font = KbitFont()
        font.props.em_ascent = stream.read_int32()
        font.props.em_descent = stream.read_int32()
        font.props.line_ascent = stream.read_int32()
        font.props.line_descent = stream.read_int32()
        font.props.line_gap = stream.read_int32()
        font.props.x_height = stream.read_int32()

        while True:
            block_type = stream.read(4)
            if block_type == kbits.BLOCK_TYPE_NAME:
                if stream.read_uint32() != kbits.SPEC_VERSION:
                    raise KbitsError('bad spec version')
                name_id = stream.read_int32()
                value = stream.read_utf()
                font.names[name_id] = value
            elif block_type == kbits.BLOCK_TYPE_CHAR:
                if stream.read_uint32() != kbits.SPEC_VERSION:
                    raise KbitsError('bad spec version')
                code_point = stream.read_int32()
                advance = stream.read_int32()
                x = stream.read_int32()
                y = stream.read_int32()
                bitmap = []
                for _ in range(stream.read_uint32()):
                    bitmap_row = []
                    for _ in range(stream.read_uint32()):
                        bitmap_row.append(stream.read_uint8())
                    bitmap.append(bitmap_row)
                font.characters[code_point] = KbitGlyph(x, y, advance, bitmap)
            elif block_type == kbits.BLOCK_TYPE_FIN:
                break
            else:
                raise KbitsError(f'bad block type: {repr(block_type)}')

        return font

    @staticmethod
    def load_kbits(file_path: str | PathLike[str]) -> KbitFont:
        with open(file_path, 'rb') as file:
            return KbitFont.parse_kbits(file)

    @staticmethod
    def parse_kbitx(stream: bytes | bytearray | BinaryIO) -> KbitFont:
        if isinstance(stream, (bytes, bytearray)):
            stream = BytesIO(stream)

        tree = etree.parse(stream)
        if tree.docinfo.root_name != kbitx.TAG_ROOT:
            raise KbitxError(f'unknown root: {repr(tree.docinfo.root_name)}')
        root = tree.getroot()

        font = KbitFont()
        for node in root:
            if node.tag == kbitx.TAG_PROP:
                value = kbitx.get_attr_int(node, kbitx.ATTR_VALUE)
                if value is None:
                    continue
                name = kbitx.get_attr_str(node, kbitx.ATTR_ID)
                if name == kbitx.PROP_EM_ASCENT:
                    font.props.em_ascent = value
                elif name == kbitx.PROP_EM_DESCENT:
                    font.props.em_descent = value
                elif name == kbitx.PROP_LINE_ASCENT:
                    font.props.line_ascent = value
                elif name == kbitx.PROP_LINE_DESCENT:
                    font.props.line_descent = value
                elif name == kbitx.PROP_LINE_GAP:
                    font.props.line_gap = value
                elif name == kbitx.PROP_X_HEIGHT:
                    font.props.x_height = value
                elif name == kbitx.PROP_CAP_HEIGHT:
                    font.props.cap_height = value
            elif node.tag == kbitx.TAG_NAME:
                name_id = kbitx.get_attr_int(node, kbitx.ATTR_ID)
                value = kbitx.get_attr_str(node, kbitx.ATTR_VALUE)
                if name_id is not None and value is not None:
                    font.names[name_id] = value
            elif node.tag == kbitx.TAG_GLYPH:
                code_point = kbitx.get_attr_int(node, kbitx.ATTR_UNICODE)
                glyph_name = kbitx.get_attr_str(node, kbitx.ATTR_NAME)
                if code_point is None and glyph_name is None:
                    continue
                x = kbitx.get_attr_int(node, kbitx.ATTR_X, 0)
                y = kbitx.get_attr_int(node, kbitx.ATTR_Y, 0)
                advance = kbitx.get_attr_int(node, kbitx.ATTR_ADVANCE, 0)
                data = kbitx.get_attr_str(node, kbitx.ATTR_DATA)
                if data is not None:
                    bitmap = Stream(base64.decode_no_padding(data.encode())).read_bitmap()
                else:
                    bitmap = None
                glyph = KbitGlyph(x, y, advance, bitmap)
                if code_point is not None:
                    font.characters[code_point] = glyph
                elif glyph_name is not None:
                    font.named_glyphs[glyph_name] = glyph
            elif node.tag == kbitx.TAG_KERN:
                offset = kbitx.get_attr_int(node, kbitx.ATTR_OFFSET)
                if offset is None:
                    continue
                left_code_point = kbitx.get_attr_int(node, kbitx.ATTR_LEFT_UNICODE)
                left_glyph_name = kbitx.get_attr_str(node, kbitx.ATTR_LEFT_NAME)
                right_code_point = kbitx.get_attr_int(node, kbitx.ATTR_RIGHT_UNICODE)
                right_glyph_name = kbitx.get_attr_str(node, kbitx.ATTR_RIGHT_NAME)
                if left_code_point is not None:
                    if right_code_point is not None:
                        font.kern_pairs[(left_code_point, right_code_point)] = offset
                    elif right_glyph_name is not None:
                        font.kern_pairs[(left_code_point, right_glyph_name)] = offset
                elif left_glyph_name is not None:
                    if right_code_point is not None:
                        font.kern_pairs[(left_glyph_name, right_code_point)] = offset
                    elif right_glyph_name is not None:
                        font.kern_pairs[(left_glyph_name, right_glyph_name)] = offset
        return font

    @staticmethod
    def load_kbitx(file_path: str | PathLike[str]) -> KbitFont:
        with open(file_path, 'rb') as file:
            return KbitFont.parse_kbitx(file)

    props: KbitProps
    names: KbitNames
    characters: dict[int, KbitGlyph]
    named_glyphs: dict[str, KbitGlyph]
    kern_pairs: dict[tuple[int | str, int | str], int]

    def __init__(
            self,
            props: KbitProps | None = None,
            names: KbitNames | None = None,
            characters: dict[int, KbitGlyph] | None = None,
            named_glyphs: dict[str, KbitGlyph] | None = None,
            kern_pairs: dict[tuple[int | str, int | str], int] | None = None,
    ):
        self.props = KbitProps() if props is None else props
        self.names = KbitNames() if names is None else names
        self.characters = {} if characters is None else characters
        self.named_glyphs = {} if named_glyphs is None else named_glyphs
        self.kern_pairs = {} if kern_pairs is None else kern_pairs

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, KbitFont):
            return NotImplemented
        return (self.props == other.props and
                self.names == other.names and
                self.characters == other.characters and
                self.named_glyphs == other.named_glyphs and
                self.kern_pairs == other.kern_pairs)

    def dump_kbits(self, stream: BinaryIO):
        stream = Stream(stream)

        stream.write(kbits.MAGIC_NUMBER)
        stream.write_uint32(kbits.SPEC_VERSION)

        stream.write_int32(self.props.em_ascent)
        stream.write_int32(self.props.em_descent)
        stream.write_int32(self.props.line_ascent)
        stream.write_int32(self.props.line_descent)
        stream.write_int32(self.props.line_gap)
        stream.write_int32(self.props.x_height)

        for name_id, value in sorted(self.names.items()):
            stream.write(kbits.BLOCK_TYPE_NAME)
            stream.write_uint32(kbits.SPEC_VERSION)
            stream.write_int32(name_id)
            stream.write_utf(value)

        for code_point, glyph in sorted(self.characters.items()):
            stream.write(kbits.BLOCK_TYPE_CHAR)
            stream.write_uint32(kbits.SPEC_VERSION)
            stream.write_int32(code_point)
            stream.write_int32(glyph.advance)
            stream.write_int32(glyph.x)
            stream.write_int32(glyph.y)
            stream.write_uint32(len(glyph.bitmap))
            for bitmap_row in glyph.bitmap:
                stream.write_uint32(len(bitmap_row))
                for color in bitmap_row:
                    stream.write_uint8(color)

        stream.write(kbits.BLOCK_TYPE_FIN)

    def dump_kbits_to_bytes(self) -> bytes:
        stream = BytesIO()
        self.dump_kbits(stream)
        return stream.getvalue()

    def save_kbits(self, file_path: str | PathLike[str]):
        with open(file_path, 'wb') as file:
            self.dump_kbits(file)

    def dump_kbitx(self, stream: BinaryIO):
        stream.write(kbitx.XML_HEADER)
        stream.write(kbitx.XML_DOCTYPE)
        stream.write(kbitx.XML_ROOT_START)

        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_EM_ASCENT),
            (kbitx.ATTR_VALUE, self.props.em_ascent),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_EM_DESCENT),
            (kbitx.ATTR_VALUE, self.props.em_descent),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_LINE_ASCENT),
            (kbitx.ATTR_VALUE, self.props.line_ascent),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_LINE_DESCENT),
            (kbitx.ATTR_VALUE, self.props.line_descent),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_LINE_GAP),
            (kbitx.ATTR_VALUE, self.props.line_gap),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_X_HEIGHT),
            (kbitx.ATTR_VALUE, self.props.x_height),
        ])
        kbitx.write_xml_tag_line(stream, kbitx.TAG_PROP, [
            (kbitx.ATTR_ID, kbitx.PROP_CAP_HEIGHT),
            (kbitx.ATTR_VALUE, self.props.cap_height),
        ])

        for name_id, value in sorted(self.names.items()):
            kbitx.write_xml_tag_line(stream, kbitx.TAG_NAME, [
                (kbitx.ATTR_ID, name_id),
                (kbitx.ATTR_VALUE, value),
            ])

        for code_point, glyph in sorted(self.characters.items()):
            data = BytesIO()
            Stream(data).write_bitmap(glyph.bitmap)
            data = base64.encode_no_padding(data.getvalue()).decode()
            kbitx.write_xml_tag_line(stream, kbitx.TAG_GLYPH, [
                (kbitx.ATTR_UNICODE, code_point),
                (kbitx.ATTR_X, glyph.x),
                (kbitx.ATTR_Y, glyph.y),
                (kbitx.ATTR_ADVANCE, glyph.advance),
                (kbitx.ATTR_DATA, data),
            ])

        for glyph_name, glyph in sorted(self.named_glyphs.items()):
            data = BytesIO()
            Stream(data).write_bitmap(glyph.bitmap)
            data = base64.encode_no_padding(data.getvalue()).decode()
            kbitx.write_xml_tag_line(stream, kbitx.TAG_GLYPH, [
                (kbitx.ATTR_NAME, glyph_name),
                (kbitx.ATTR_X, glyph.x),
                (kbitx.ATTR_Y, glyph.y),
                (kbitx.ATTR_ADVANCE, glyph.advance),
                (kbitx.ATTR_DATA, data),
            ])

        for (left, right), offset in sorted(self.kern_pairs.items(), key=_kern_pairs_key_comparator):
            if isinstance(left, int):
                if isinstance(right, int):
                    kbitx.write_xml_tag_line(stream, kbitx.TAG_KERN, [
                        (kbitx.ATTR_LEFT_UNICODE, left),
                        (kbitx.ATTR_RIGHT_UNICODE, right),
                        (kbitx.ATTR_OFFSET, offset),
                    ])
                elif isinstance(right, str):
                    kbitx.write_xml_tag_line(stream, kbitx.TAG_KERN, [
                        (kbitx.ATTR_LEFT_UNICODE, left),
                        (kbitx.ATTR_RIGHT_NAME, right),
                        (kbitx.ATTR_OFFSET, offset),
                    ])
            elif isinstance(left, str):
                if isinstance(right, int):
                    kbitx.write_xml_tag_line(stream, kbitx.TAG_KERN, [
                        (kbitx.ATTR_LEFT_NAME, left),
                        (kbitx.ATTR_RIGHT_UNICODE, right),
                        (kbitx.ATTR_OFFSET, offset),
                    ])
                elif isinstance(right, str):
                    kbitx.write_xml_tag_line(stream, kbitx.TAG_KERN, [
                        (kbitx.ATTR_LEFT_NAME, left),
                        (kbitx.ATTR_RIGHT_NAME, right),
                        (kbitx.ATTR_OFFSET, offset),
                    ])

        stream.write(kbitx.XML_ROOT_CLOSE)

    def dump_kbitx_to_bytes(self) -> bytes:
        stream = BytesIO()
        self.dump_kbitx(stream)
        return stream.getvalue()

    def save_kbitx(self, file_path: str | PathLike[str]):
        with open(file_path, 'wb') as file:
            self.dump_kbitx(file)
