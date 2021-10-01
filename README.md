# BytesIOEx

BytesIOEx is a simple wrapper over Python's `io.BytesIO` which provides additional methods for reading and writing C data types like **int8**, **uint8**, **bool** and so on. The `read_*` methods are used for reading a particular type from the stream and the `write_*` methods are used for writing Python's basic data types **int**, **bool** and **float** to the stream. Both these types of methods advance the steam position by the size of the data type. The type conversion is handled by the `struct` module. `Struct` classes are used to maximize the performance. **Native byteorder is used.**

## Note

To mimick the behavior of `BytesIO.read` method, the `read_*` methods return `None` when sufficient number of bytes are not available for reading a type.

To mimick the behavior of `BytesIO.write` method, the `write_*` methods return the value returned by `BytesIO.write`.

## Reference

`read_*` methods:
* `read_bool` - Reads a C99-style _Bool type, *where 0 = False, else True*.
* `read_int8` - Reads a signed 8-bit integer.
* `read_uint8` - Reads an unsigned 8-bit integer.
* `read_char` - Reads an 8-bit ASCII character. *Analogous to calling `chr(read_uint8())`*.
* `read_int16` - Reads a signed 16-bit integer.
* `read_uint16` - Reads an unsigned 16-bit integer.
* `read_int32` - Reads a signed 32-bit integer.
* `read_uint32` - Reads an unsigned 32-bit integer.
* `read_int64` - Reads a signed 64-bit integer.
* `read_uint64` - Reads an unsigned 64-bit integer.
* `read_float` - Reads a 4-byte floating-point number.
* `read_double` - Reads an 8-byte floating-point number.
* `read_varint` - Reads a 7-bit encoded integer, *the exact size of this type is not fixed*. If the stream pointer reaches the end before being completely able to read, it will return `None`.

`write_*` methods:
* `write_bool` - Converts and writes a Python `bool` into a C99-style _Bool type, *where False = 0, True = 1*.
* `write_int8` - Converts and writes a Python `int` into a signed 8-bit integer.
* `write_uint8` - Converts and writes a Python `int` into an unsigned 8-bit integer.
* `write_char` - Converts and writes a Python `str` into an 8-bit ASCII character.
* `write_int16` - Converts and writes a Python `int` into a signed 16-bit integer.
* `write_uint16` - Converts and writes a Python `int` into an unsigned 16-bit integer.
* `write_int32` - Converts and writes a Python `int` into a signed 32-bit integer.
* `write_uint32` - Converts and writes a Python `int` into an unsigned 32-bit integer.
* `write_int64` - Converts and writes a Python `int` into a signed 64-bit integer.
* `write_uint64` - Converts and writes a Python `int` into an unsigned 64-bit integer.
* `write_float` - Converts and writes a Python `float` into a 4-byte floating-point number.
* `write_double` - Converts and writes a Python `float` into an 8-byte floating-point number.
* `write_varint` - Converts and writes a Python `int` into a 7-bit encoded integer (varint).

## Motivation
C# `BinaryReader` and `BinaryWriter`