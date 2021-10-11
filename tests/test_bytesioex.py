from bytesioex import BytesIOEx


class TestBytesIOEx:
    B = b"\xFF"
    H = b"\xFF\xFF"

    def test_read_uint8(self):
        b = BytesIOEx(self.B)
        assert b.read_B() == 255

    def test_read_int8(self):
        b = BytesIOEx(self.B)
        assert b.read_b() == -1

    def test_read_uint16(self):
        b = BytesIOEx(self.H)
        assert b.read_H() == 65535

    def test_read_int16(self):
        b = BytesIOEx(self.H)
        assert b.read_h() == -1
