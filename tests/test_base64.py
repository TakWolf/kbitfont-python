from kbitfont.internal import base64


def test_base64():
    plain = 'Hello World'
    encoded = 'SGVsbG8gV29ybGQ'
    assert base64.encode_no_padding(plain.encode()).decode() == encoded
    assert base64.decode_no_padding(encoded.encode()).decode() == plain
