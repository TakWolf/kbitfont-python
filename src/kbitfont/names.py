from collections import UserDict
from typing import Any

_NAME_COPYRIGHT = 0
_NAME_FAMILY = 1
_NAME_STYLE = 2
_NAME_UNIQUE_ID = 3
_NAME_FAMILY_AND_STYLE = 4
_NAME_VERSION = 5
_NAME_POSTSCRIPT = 6
_NAME_TRADEMARK = 7
_NAME_MANUFACTURER = 8
_NAME_DESIGNER = 9
_NAME_DESCRIPTION = 10
_NAME_VENDOR_URL = 11
_NAME_DESIGNER_URL = 12
_NAME_LICENSE_DESCRIPTION = 13
_NAME_LICENSE_URL = 14
_NAME_WINDOWS_FAMILY = 16
_NAME_WINDOWS_STYLE = 17
_NAME_MACOS_FAMILY_AND_STYLE = 18
_NAME_SAMPLE_TEXT = 19
_NAME_POSTSCRIPT_CID = 20
_NAME_WWS_FAMILY = 21
_NAME_WWS_STYLE = 22

_NAMES = {
    _NAME_COPYRIGHT,
    _NAME_FAMILY,
    _NAME_STYLE,
    _NAME_UNIQUE_ID,
    _NAME_FAMILY_AND_STYLE,
    _NAME_VERSION,
    _NAME_POSTSCRIPT,
    _NAME_TRADEMARK,
    _NAME_MANUFACTURER,
    _NAME_DESIGNER,
    _NAME_DESCRIPTION,
    _NAME_VENDOR_URL,
    _NAME_DESIGNER_URL,
    _NAME_LICENSE_DESCRIPTION,
    _NAME_LICENSE_URL,
    _NAME_WINDOWS_FAMILY,
    _NAME_WINDOWS_STYLE,
    _NAME_MACOS_FAMILY_AND_STYLE,
    _NAME_SAMPLE_TEXT,
    _NAME_POSTSCRIPT_CID,
    _NAME_WWS_FAMILY,
    _NAME_WWS_STYLE,
}


class KbitNames(UserDict[int, str]):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key: Any, value: Any):
        if key not in _NAMES:
            raise KeyError(key)

        if value is None:
            self.pop(key, None)
            return

        if not isinstance(value, str):
            raise ValueError(value)

        super().__setitem__(key, value)

    @property
    def copyright(self) -> str | None:
        return self.get(_NAME_COPYRIGHT, None)

    @copyright.setter
    def copyright(self, value: str | None):
        self[_NAME_COPYRIGHT] = value

    @property
    def family(self) -> str | None:
        return self.get(_NAME_FAMILY, None)

    @family.setter
    def family(self, value: str | None):
        self[_NAME_FAMILY] = value

    @property
    def style(self) -> str | None:
        return self.get(_NAME_STYLE, None)

    @style.setter
    def style(self, value: str | None):
        self[_NAME_STYLE] = value

    @property
    def unique_id(self) -> str | None:
        return self.get(_NAME_UNIQUE_ID, None)

    @unique_id.setter
    def unique_id(self, value: str | None):
        self[_NAME_UNIQUE_ID] = value

    @property
    def family_and_style(self) -> str | None:
        return self.get(_NAME_FAMILY_AND_STYLE, None)

    @family_and_style.setter
    def family_and_style(self, value: str | None):
        self[_NAME_FAMILY_AND_STYLE] = value

    @property
    def version(self) -> str | None:
        return self.get(_NAME_VERSION, None)

    @version.setter
    def version(self, value: str | None):
        self[_NAME_VERSION] = value

    @property
    def postscript(self) -> str | None:
        return self.get(_NAME_POSTSCRIPT, None)

    @postscript.setter
    def postscript(self, value: str | None):
        self[_NAME_POSTSCRIPT] = value

    @property
    def trademark(self) -> str | None:
        return self.get(_NAME_TRADEMARK, None)

    @trademark.setter
    def trademark(self, value: str | None):
        self[_NAME_TRADEMARK] = value

    @property
    def manufacturer(self) -> str | None:
        return self.get(_NAME_MANUFACTURER, None)

    @manufacturer.setter
    def manufacturer(self, value: str | None):
        self[_NAME_MANUFACTURER] = value

    @property
    def designer(self) -> str | None:
        return self.get(_NAME_DESIGNER, None)

    @designer.setter
    def designer(self, value: str | None):
        self[_NAME_DESIGNER] = value

    @property
    def description(self) -> str | None:
        return self.get(_NAME_DESCRIPTION, None)

    @description.setter
    def description(self, value: str | None):
        self[_NAME_DESCRIPTION] = value

    @property
    def vendor_url(self) -> str | None:
        return self.get(_NAME_VENDOR_URL, None)

    @vendor_url.setter
    def vendor_url(self, value: str | None):
        self[_NAME_VENDOR_URL] = value

    @property
    def designer_url(self) -> str | None:
        return self.get(_NAME_DESIGNER_URL, None)

    @designer_url.setter
    def designer_url(self, value: str | None):
        self[_NAME_DESIGNER_URL] = value

    @property
    def license_description(self) -> str | None:
        return self.get(_NAME_LICENSE_DESCRIPTION, None)

    @license_description.setter
    def license_description(self, value: str | None):
        self[_NAME_LICENSE_DESCRIPTION] = value

    @property
    def license_url(self) -> str | None:
        return self.get(_NAME_LICENSE_URL, None)

    @license_url.setter
    def license_url(self, value: str | None):
        self[_NAME_LICENSE_URL] = value

    @property
    def windows_family(self) -> str | None:
        return self.get(_NAME_WINDOWS_FAMILY, None)

    @windows_family.setter
    def windows_family(self, value: str | None):
        self[_NAME_WINDOWS_FAMILY] = value

    @property
    def windows_style(self) -> str | None:
        return self.get(_NAME_WINDOWS_STYLE, None)

    @windows_style.setter
    def windows_style(self, value: str | None):
        self[_NAME_WINDOWS_STYLE] = value

    @property
    def macos_family_and_style(self) -> str | None:
        return self.get(_NAME_MACOS_FAMILY_AND_STYLE, None)

    @macos_family_and_style.setter
    def macos_family_and_style(self, value: str | None):
        self[_NAME_MACOS_FAMILY_AND_STYLE] = value

    @property
    def sample_text(self) -> str | None:
        return self.get(_NAME_SAMPLE_TEXT, None)

    @sample_text.setter
    def sample_text(self, value: str | None):
        self[_NAME_SAMPLE_TEXT] = value

    @property
    def postscript_cid(self) -> str | None:
        return self.get(_NAME_POSTSCRIPT_CID, None)

    @postscript_cid.setter
    def postscript_cid(self, value: str | None):
        self[_NAME_POSTSCRIPT_CID] = value

    @property
    def wws_family(self) -> str | None:
        return self.get(_NAME_WWS_FAMILY, None)

    @wws_family.setter
    def wws_family(self, value: str | None):
        self[_NAME_WWS_FAMILY] = value

    @property
    def wws_style(self) -> str | None:
        return self.get(_NAME_WWS_STYLE, None)

    @wws_style.setter
    def wws_style(self, value: str | None):
        self[_NAME_WWS_STYLE] = value
