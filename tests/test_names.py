from copy import copy, deepcopy

from kbitfont import KbitNames


def test_names():
    names = KbitNames()

    names.copyright = 'ID: 0'
    assert names.copyright == 'ID: 0'
    assert names[0] == 'ID: 0'

    names.family = 'ID: 1'
    assert names.family == 'ID: 1'
    assert names[1] == 'ID: 1'

    names.style = 'ID: 2'
    assert names.style == 'ID: 2'
    assert names[2] == 'ID: 2'

    names.unique_id = 'ID: 3'
    assert names.unique_id == 'ID: 3'
    assert names[3] == 'ID: 3'

    names.family_and_style = 'ID: 4'
    assert names.family_and_style == 'ID: 4'
    assert names[4] == 'ID: 4'

    names.version = 'ID: 5'
    assert names.version == 'ID: 5'
    assert names[5] == 'ID: 5'

    names.postscript = 'ID: 6'
    assert names.postscript == 'ID: 6'
    assert names[6] == 'ID: 6'

    names.trademark = 'ID: 7'
    assert names.trademark == 'ID: 7'
    assert names[7] == 'ID: 7'

    names.manufacturer = 'ID: 8'
    assert names.manufacturer == 'ID: 8'
    assert names[8] == 'ID: 8'

    names.designer = 'ID: 9'
    assert names.designer == 'ID: 9'
    assert names[9] == 'ID: 9'

    names.description = 'ID: 10'
    assert names.description == 'ID: 10'
    assert names[10] == 'ID: 10'

    names.vendor_url = 'ID: 11'
    assert names.vendor_url == 'ID: 11'
    assert names[11] == 'ID: 11'

    names.designer_url = 'ID: 12'
    assert names.designer_url == 'ID: 12'
    assert names[12] == 'ID: 12'

    names.license_description = 'ID: 13'
    assert names.license_description == 'ID: 13'
    assert names[13] == 'ID: 13'

    names.license_url = 'ID: 14'
    assert names.license_url == 'ID: 14'
    assert names[14] == 'ID: 14'

    names.windows_family = 'ID: 16'
    assert names.windows_family == 'ID: 16'
    assert names[16] == 'ID: 16'

    names.windows_style = 'ID: 17'
    assert names.windows_style == 'ID: 17'
    assert names[17] == 'ID: 17'

    names.macos_family_and_style = 'ID: 18'
    assert names.macos_family_and_style == 'ID: 18'
    assert names[18] == 'ID: 18'

    names.sample_text = 'ID: 19'
    assert names.sample_text == 'ID: 19'
    assert names[19] == 'ID: 19'

    names.postscript_cid = 'ID: 20'
    assert names.postscript_cid == 'ID: 20'
    assert names[20] == 'ID: 20'

    names.wws_family = 'ID: 21'
    assert names.wws_family == 'ID: 21'
    assert names[21] == 'ID: 21'

    names.wws_style = 'ID: 22'
    assert names.wws_style == 'ID: 22'
    assert names[22] == 'ID: 22'


def test_copy():
    names_1 = KbitNames()
    names_1.copyright = 'ID: 0'
    names_1.family = 'ID: 1'
    names_2 = copy(names_1)
    names_3 = deepcopy(names_1)

    assert names_1 == names_2
    assert names_1 == names_3
    assert names_1 is not names_2
    assert names_1 is not names_3


def test_eq():
    names_1 = KbitNames()
    names_1.copyright = 'ID: 0'
    names_1.family = 'ID: 1'

    names_2 = KbitNames()
    names_2.copyright = 'ID: 0'
    names_2.family = 'ID: 1'

    assert names_1 == names_2
