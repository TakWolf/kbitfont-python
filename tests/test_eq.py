from pathlib import Path

from kbitfont import KbitFont


def test_demo_kbits(assets_dir: Path, tmp_path: Path):
    file_path = assets_dir.joinpath('demo', 'demo.kbits')
    font_1 = KbitFont.load_kbits(file_path)
    font_2 = KbitFont.load_kbits(file_path)
    assert font_1 == font_2


def test_demo_kbitx(assets_dir: Path, tmp_path: Path):
    file_path = assets_dir.joinpath('demo', 'demo.kbitx')
    font_1 = KbitFont.load_kbitx(file_path)
    font_2 = KbitFont.load_kbitx(file_path)
    assert font_1 == font_2
