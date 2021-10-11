import io
from struct import Struct
from typing import Optional

# Converters
Bool = Struct("?")
Char = Struct("c")
SByte = Struct("b")
Byte = Struct("B")
Short = Struct("h")
UShort = Struct("H")
Int = Struct("i")
UInt = Struct("I")
Long = Struct("q")
ULong = Struct("Q")
Float = Struct("f")
Double = Struct("d")


class BytesIOEx(io.BytesIO):
    """A simple wrapper over Python's `io.BytesIO` which provides additional
    methods for reading and writing C data types like `int8`, `uint8`, `bool`,
    `float`, `double` etc."""

    def read_bool(self) -> Optional[bool]:
        """Reads a C99 _Bool."""
        buf = self.read(1)
        return Bool.unpack(buf)[0] if len(buf) == 1 else None

    def read_b(self) -> Optional[int]:
        """Reads a 1-byte signed integer."""
        buf = self.read(1)
        return SByte.unpack(buf)[0] if len(buf) == 1 else None

    def read_B(self) -> Optional[int]:
        """Reads a 1-byte unsigned integer."""
        buf = self.read(1)
        return Byte.unpack(buf)[0] if len(buf) == 1 else None

    def read_c(self) -> Optional[str]:
        """Reads a 1-byte ASCII-character."""
        buf = self.read(1)
        return Char.unpack(buf)[0] if len(buf) == 1 else None

    def read_h(self) -> Optional[int]:
        """Reads a 2-byte signed integer."""
        buf = self.read(2)
        return Short.unpack(buf)[0] if len(buf) == 2 else None

    def read_H(self) -> Optional[int]:
        """Reads a 2-byte unsigned integer."""
        buf = self.read(2)
        return UShort.unpack(buf)[0] if len(buf) == 2 else None

    def read_i(self) -> Optional[int]:
        """Reads a 4-byte signed integer."""
        buf = self.read(4)
        return Int.unpack(buf)[0] if len(buf) == 4 else None

    def read_I(self) -> Optional[int]:
        """Reads a 4-byte unsigned integer."""
        buf = self.read(4)
        return UInt.unpack(buf)[0] if len(buf) == 4 else None

    def read_q(self) -> Optional[int]:
        """Reads an 8-byte signed integer."""
        buf = self.read(8)
        return Long.unpack(buf)[0] if len(buf) == 8 else None

    def read_Q(self) -> Optional[int]:
        """Reads an 8-byte unsigned integer."""
        buf = self.read(8)
        return ULong.unpack(buf)[0] if len(buf) == 8 else None

    def read_f(self) -> Optional[float]:
        """Reads a 4-byte floating-point number."""
        buf = self.read(4)
        return Float.unpack(buf)[0] if len(buf) == 4 else None

    def read_d(self) -> Optional[float]:
        """Reads an 8-byte floating-point number."""
        buf = self.read(8)
        return Double.unpack(buf)[0] if len(buf) == 8 else None

    def read_v(self) -> Optional[int]:
        """Reads a 7-bit encoded integer, the exact size of this type is not
        fixed, hence the name **varint**. If the stream pointer reaches the
        end before being completely able to read, it will return None."""
        b = self.read_B()
        if b is not None:
            data_len = b & 0x7F
            shift = 7
            while (b & 0x80) != 0:
                b = self.read_B()
                if b is None:
                    return None
                data_len |= (b & 0x7F) << shift
                shift += 7
            return data_len
        return None

    def write_bool(self, value: bool) -> int:
        """Converts and writes a `bool` into a C99-style _Bool type,
        where False = 0, True = 1."""
        return self.write(Bool.pack(value))

    def write_b(self, value: int) -> int:
        """Converts and writes a `int` into a signed 8-bit integer."""
        return self.write(SByte.pack(value))

    def write_B(self, value: int) -> int:
        """Converts and writes a `int` into an unsigned 8-bit integer."""
        return self.write(Byte.pack(value))

    def write_c(self, value: str) -> int:
        """Converts and writes a `int` into an unsigned 8-bit integer."""
        return self.write(Char.pack(value))

    def write_h(self, value: int) -> int:
        """Converts and writes a `int` into a signed 16-bit integer."""
        return self.write(Short.pack(value))

    def write_H(self, value: int) -> int:
        """Converts and writes a `int` into an unsigned 16-bit integer."""
        return self.write(UShort.pack(value))

    def write_i(self, value: int) -> int:
        """Converts and writes a `int` into a signed 32-bit integer."""
        return self.write(Int.pack(value))

    def write_I(self, value: int) -> int:
        """Converts and writes a `int` into an unsigned 32-bit integer."""
        return self.write(UInt.pack(value))

    def write_q(self, value: int) -> int:
        """Converts and writes a `int` into a signed 64-bit integer."""
        return self.write(Long.pack(value))

    def write_Q(self, value: int) -> int:
        """Converts and writes a `int` into an unsigned 64-bit integer."""
        return self.write(ULong.pack(value))

    def write_f(self, value: float) -> int:
        """Converts and writes a `float` into a 4-byte floating-point number."""
        return self.write(Float.pack(value))

    def write_d(self, value: float) -> int:
        """Converts and writes a `float` into an 8-byte floating-point number."""
        return self.write(Double.pack(value))

    def write_v(self, buflen: int) -> int:
        """Converts an unsigned integer to a 7-bit encoded integer (varint)
        and writes it.

        Args:
            buflen (int): The length of the buffer to be converted and written.
        """
        ret = bytearray()
        while True:
            towrite = buflen & 0x7F
            buflen >>= 7
            if buflen > 0:
                towrite |= 0x80
            ret.append(towrite)
            if buflen <= 0:
                break
        return self.write(bytes(ret))
