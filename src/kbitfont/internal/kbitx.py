from typing import Final

from lxml.etree import Element

TAG_ROOT: Final = 'kbits'
TAG_PROP: Final = 'prop'
TAG_NAME: Final = 'name'
TAG_GLYPH: Final = 'g'
TAG_KERN: Final = 'k'

ATTR_ID: Final = 'id'
ATTR_VALUE: Final = 'value'
ATTR_UNICODE: Final = 'u'
ATTR_NAME: Final = 'n'
ATTR_X: Final = 'x'
ATTR_Y: Final = 'y'
ATTR_ADVANCE: Final = 'w'
ATTR_DATA: Final = 'd'
ATTR_LEFT_UNICODE: Final = 'lu'
ATTR_LEFT_NAME: Final = 'ln'
ATTR_RIGHT_UNICODE: Final = 'ru'
ATTR_RIGHT_NAME: Final = 'rn'
ATTR_OFFSET: Final = 'o'

PROP_EM_ASCENT: Final = 'emAscent'
PROP_EM_DESCENT: Final = 'emDescent'
PROP_LINE_ASCENT: Final = 'lineAscent'
PROP_LINE_DESCENT: Final = 'lineDescent'
PROP_LINE_GAP: Final = 'lineGap'
PROP_X_HEIGHT: Final = 'xHeight'
PROP_CAP_HEIGHT: Final = 'capHeight'


def get_attr_str(node: Element, key: str, default: str = None) -> str | None:
    value = node.attrib.get(key, None)
    if value is not None:
        value = value.strip()
        if value != '':
            return value
    return default


def get_attr_int(node: Element, key: str, default: int = None) -> int | None:
    value = get_attr_str(node, key)
    if value is not None:
        return int(value)
    return default
