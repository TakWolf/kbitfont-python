from pathlib import Path

import pytest

from kbitfont import KbitFont


@pytest.mark.parametrize(
    'font_dir, font_file_name', [
        ('demo', 'demo.kbits'),
        ('macintosh', 'Athens.kbits'),
        ('macintosh', 'Geneva-12.kbits'),
        ('macintosh', 'New-York-14.kbits'),
    ],
)
def test_load_save_kbits(assets_dir: Path, tmp_path: Path, font_dir: str, font_file_name: str):
    load_path = assets_dir.joinpath(font_dir, font_file_name)
    save_path = tmp_path.joinpath(font_file_name)
    font = KbitFont.load_kbits(load_path)
    font.save_kbits(save_path)
    assert load_path.read_bytes() == save_path.read_bytes()


@pytest.mark.parametrize(
    'font_dir, font_file_name', [
        ('demo', 'demo.kbitx'),
        ('macintosh', 'Athens.kbitx'),
        ('macintosh', 'Geneva-12.kbitx'),
        ('macintosh', 'New-York-14.kbitx'),
    ],
)
def test_load_save_kbitx(assets_dir: Path, tmp_path: Path, font_dir: str, font_file_name: str):
    load_path = assets_dir.joinpath(font_dir, font_file_name)
    save_path = tmp_path.joinpath(font_file_name)
    font = KbitFont.load_kbitx(load_path)
    font.save_kbitx(save_path)
    assert load_path.read_bytes().replace(b'\r\n', b'\n') == save_path.read_bytes()
