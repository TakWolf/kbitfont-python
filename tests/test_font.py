from copy import copy, deepcopy
from pathlib import Path

from kbitfont import KbitFont


def test_copy(assets_dir: Path):
    font_1 = KbitFont.load_kbitx(assets_dir.joinpath('demo', 'demo.kbitx'))
    font_2 = copy(font_1)

    assert font_1 == font_2
    assert font_1 is not font_2
    assert font_1.props is font_2.props
    assert font_1.names is font_2.names
    assert font_1.characters is font_2.characters
    assert font_1.named_glyphs is font_2.named_glyphs
    assert font_1.kern_pairs is font_2.kern_pairs


def test_deepcopy(assets_dir: Path):
    font_1 = KbitFont.load_kbitx(assets_dir.joinpath('demo', 'demo.kbitx'))
    font_2 = deepcopy(font_1)

    assert font_1 == font_2
    assert font_1 is not font_2
    assert font_1.props is not font_2.props
    assert font_1.names is not font_2.names
    assert font_1.characters is not font_2.characters
    assert font_1.named_glyphs is not font_2.named_glyphs
    assert font_1.kern_pairs is not font_2.kern_pairs

    for (code_point_1, glyph_1), (code_point_2, glyph_2) in zip(sorted(font_1.characters.items()), sorted(font_2.characters.items())):
        assert code_point_1 == code_point_2
        assert glyph_1 is not glyph_2

    for (glyph_name_1, glyph_1), (glyph_name_2, glyph_2) in zip(sorted(font_1.named_glyphs.items()), sorted(font_2.named_glyphs.items())):
        assert glyph_name_1 == glyph_name_2
        assert glyph_1 is not glyph_2


def test_eq(assets_dir: Path):
    file_path = assets_dir.joinpath('demo', 'demo.kbitx')
    font_1 = KbitFont.load_kbitx(file_path)
    font_2 = KbitFont.load_kbitx(file_path)
    assert font_1 == font_2
