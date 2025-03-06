from io import BytesIO
from os import PathLike
from typing import BinaryIO

from kbitfont.glyph import KbitGlyph
from kbitfont.names import KbitNames
from kbitfont.props import KbitProps


class KbitFont:
    @staticmethod
    def parse_kbits(stream: bytes | BinaryIO) -> 'KbitFont':
        # TODO
        return KbitFont()

    @staticmethod
    def load_kbits(file_path: str | PathLike[str]) -> 'KbitFont':
        with open(file_path, 'rb') as file:
            return KbitFont.parse_kbits(file)

    @staticmethod
    def parse_kbitx(stream: bytes | BinaryIO) -> 'KbitFont':
        # TODO
        return KbitFont()

    @staticmethod
    def load_kbitx(file_path: str | PathLike[str]) -> 'KbitFont':
        with open(file_path, 'rb') as file:
            return KbitFont.parse_kbitx(file)

    props: KbitProps
    names: KbitNames
    characters: dict[int, KbitGlyph]
    named_glyphs: dict[str, KbitGlyph]
    kern_pairs: dict[tuple[int | str, int | str], int]

    def __init__(self):
        self.props = KbitProps()
        self.names = KbitNames()
        self.characters = {}
        self.named_glyphs = {}
        self.kern_pairs = {}

    def dump_kbits(self, stream: BinaryIO):
        # TODO
        pass

    def dump_kbits_to_bytes(self) -> bytes:
        stream = BytesIO()
        self.dump_kbits(stream)
        return stream.getvalue()

    def save_kbits(self, file_path: str | PathLike[str]):
        with open(file_path, 'wb') as file:
            self.dump_kbits(file)

    def dump_kbitx(self, stream: BinaryIO):
        # TODO
        pass

    def dump_kbitx_to_bytes(self) -> bytes:
        stream = BytesIO()
        self.dump_kbitx(stream)
        return stream.getvalue()

    def save_kbitx(self, file_path: str | PathLike[str]):
        with open(file_path, 'wb') as file:
            self.dump_kbitx(file)
