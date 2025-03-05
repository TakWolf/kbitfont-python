from kbitfont.glyph import KbitGlyph
from kbitfont.names import KbitNames
from kbitfont.props import KbitProps


class KbitFont:
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
