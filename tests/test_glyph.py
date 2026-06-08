from copy import copy, deepcopy

from kbitfont import KbitGlyph


def test_glyph():
    glyph = KbitGlyph(
        x=1,
        y=2,
        advance=3,
        bitmap=[[1, 0, 0, 1]],
    )
    assert glyph.width == 4
    assert glyph.height == 1
    assert glyph.dimensions == (4, 1)


def test_copy():
    glyph_1 = KbitGlyph(
        x=1,
        y=2,
        advance=3,
        bitmap=[[1, 0, 0, 1]],
    )
    glyph_2 = copy(glyph_1)

    assert glyph_1 == glyph_2
    assert glyph_1 is not glyph_2
    assert glyph_1.bitmap is glyph_2.bitmap


def test_deepcopy():
    glyph_1 = KbitGlyph(
        x=1,
        y=2,
        advance=3,
        bitmap=[[1, 0, 0, 1]],
    )
    glyph_2 = deepcopy(glyph_1)

    assert glyph_1 == glyph_2
    assert glyph_1 is not glyph_2
    assert glyph_1.bitmap is not glyph_2.bitmap

    for bitmap_row_1, bitmap_row_2 in zip(glyph_1.bitmap, glyph_2.bitmap):
        assert bitmap_row_1 is not bitmap_row_2


def test_eq():
    glyph_1 = KbitGlyph(
        x=1,
        y=2,
        advance=3,
        bitmap=[[1, 0, 0, 1]],
    )
    glyph_2 = KbitGlyph(
        x=1,
        y=2,
        advance=3,
        bitmap=[[1, 0, 0, 1]],
    )
    assert glyph_1 == glyph_2
