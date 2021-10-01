from bytesioex import BytesIOEx

class TestBytesIOEx:
    def test_read_uint8(self):
        a = b'\x02'
        assert BytesIOEx(a).read_uint8() == 2