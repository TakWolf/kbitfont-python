from kbitfont.utils import base64


def test_base64():
    plain = b'Hello World'
    encoded = b'SGVsbG8gV29ybGQ'
    assert base64.encode_no_padding(plain) == encoded
    assert base64.decode_no_padding(encoded) == plain
