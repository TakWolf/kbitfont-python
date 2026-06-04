from pathlib import Path

from kbitfont import KbitFont


def test_demo_kbits(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('demo', 'demo.kbits')
    save_path = tmp_path.joinpath('demo.kbits')
    font = KbitFont.load_kbits(load_path)
    font.save_kbits(save_path)
    assert load_path.read_bytes() == save_path.read_bytes()


def test_demo_kbitx(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('demo', 'demo.kbitx')
    save_path = tmp_path.joinpath('demo.kbitx')
    font = KbitFont.load_kbitx(load_path)
    font.save_kbitx(save_path)
    assert load_path.read_bytes().replace(b'\r\n', b'\n') == save_path.read_bytes()


def test_athens_kbits(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'Athens.kbits')
    save_path = tmp_path.joinpath('Athens.kbits')
    font = KbitFont.load_kbits(load_path)
    font.save_kbits(save_path)
    assert load_path.read_bytes() == save_path.read_bytes()


def test_athens_kbitx(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'Athens.kbitx')
    save_path = tmp_path.joinpath('Athens.kbitx')
    font = KbitFont.load_kbitx(load_path)
    font.save_kbitx(save_path)
    assert load_path.read_bytes().replace(b'\r\n', b'\n') == save_path.read_bytes()


def test_geneva_12_kbits(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'Geneva-12.kbits')
    save_path = tmp_path.joinpath('Geneva-12.kbits')
    font = KbitFont.load_kbits(load_path)
    font.save_kbits(save_path)
    assert load_path.read_bytes() == save_path.read_bytes()


def test_geneva_12_kbitx(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'Geneva-12.kbitx')
    save_path = tmp_path.joinpath('Geneva-12.kbitx')
    font = KbitFont.load_kbitx(load_path)
    font.save_kbitx(save_path)
    assert load_path.read_bytes().replace(b'\r\n', b'\n') == save_path.read_bytes()


def test_new_york_14_kbits(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'New-York-14.kbits')
    save_path = tmp_path.joinpath('New-York-14.kbits')
    font = KbitFont.load_kbits(load_path)
    font.save_kbits(save_path)
    assert load_path.read_bytes() == save_path.read_bytes()


def test_new_york_14_kbitx(assets_dir: Path, tmp_path: Path):
    load_path = assets_dir.joinpath('macintosh', 'New-York-14.kbitx')
    save_path = tmp_path.joinpath('New-York-14.kbitx')
    font = KbitFont.load_kbitx(load_path)
    font.save_kbitx(save_path)
    assert load_path.read_bytes().replace(b'\r\n', b'\n') == save_path.read_bytes()
