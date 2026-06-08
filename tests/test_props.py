from copy import copy, deepcopy

from kbitfont import KbitProps


def test_props():
    props = KbitProps(
        em_ascent=10,
        em_descent=2,
        line_ascent=12,
        line_descent=4,
    )
    assert props.em_height == 12
    assert props.line_height == 16


def test_copy():
    props_1 = KbitProps(
        em_ascent=1,
        em_descent=2,
        line_ascent=3,
        line_descent=4,
        line_gap=5,
        x_height=6,
        cap_height=7,
    )
    props_2 = copy(props_1)
    props_3 = deepcopy(props_1)

    assert props_1 == props_2
    assert props_1 == props_3
    assert props_1 is not props_2
    assert props_1 is not props_3


def test_eq():
    props_1 = KbitProps(
        em_ascent=1,
        em_descent=2,
        line_ascent=3,
        line_descent=4,
        line_gap=5,
        x_height=6,
        cap_height=7,
    )
    props_2 = KbitProps(
        em_ascent=1,
        em_descent=2,
        line_ascent=3,
        line_descent=4,
        line_gap=5,
        x_height=6,
        cap_height=7,
    )
    assert props_1 == props_2
