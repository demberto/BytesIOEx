import unittest

from bytesioex.bytesioex import BytesIOEx

class TestBytesIOEx(unittest.TestCase):
    def test_read_bool(self):
        stream = BytesIOEx(b'\x00')
        self.assertEquals(stream.read_bool(), False)
    
    def test_write_bool(self):
        stream = BytesIOEx()
        stream.write_bool(True)
        stream.seek(0)
        self.assertEquals(stream.read_bool(), True)
    
    # TODO: More tests