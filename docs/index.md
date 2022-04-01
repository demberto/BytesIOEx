# BytesIOEx

![PyPI](https://img.shields.io/pypi/v/bytesioex)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bytesioex)
[![Code Style: Black][black]](https://github.com/psf/black)
[![security: bandit][bandit]](https://github.com/PyCQA/bandit)

BytesIOEx is a simple wrapper over Python's `io.BytesIO` which provides
additional methods for reading and writing C data types like **int8**,
**uint8**, **bool** and so on. The `read_*` methods are used for reading a
particular type from the stream and the `write_*` methods are used for writing
Python's basic data types **int**, **bool** and **float** to the stream. Both
these types of methods advance the steam position by the size of the data type.
The type conversion is handled by the `struct` module. `Struct` classes are
used to maximize the performance. **Native byteorder is used.**

## Installation

!!! tip
    BytesIOEx requires Python 3.6+, it may run on older version as well but I
    have not tested it.

```
pip install --upgrade bytesioex
```

## `read_*` methods

!!! note
    To mimick the behavior of `BytesIO.read` method, the `read_*` methods
    return `None` when sufficient number of bytes are not available for
    reading a type.

- `read_bool` - Reads a C99-style \_Bool type, _where 0 = False, else True_.
- `read_b` - Reads a signed 8-bit integer.
- `read_B` - Reads an unsigned 8-bit integer.
- `read_c` - Reads an 8-bit ASCII character. _Analogous to `chr(read_B())`_.
- `read_h` - Reads a signed 16-bit integer.
- `read_H` - Reads an unsigned 16-bit integer.
- `read_i` - Reads a signed 32-bit integer.
- `read_I` - Reads an unsigned 32-bit integer.
- `read_q` - Reads a signed 64-bit integer.
- `read_Q` - Reads an unsigned 64-bit integer.
- `read_f` - Reads a 4-byte floating-point number.
- `read_d` - Reads an 8-byte floating-point number.
- `read_v` - Reads a 7-bit encoded integer, _the exact size of this type is
  not fixed_. If the stream pointer reaches the end before being completely
  able to read, it will return `None`.

## `write_*` methods

!!! note
    To mimick the behavior of `BytesIO.write` method, the `write_*` methods
    return the value returned by `BytesIO.write`.

- `write_bool` - Converts and writes a `bool` into a C99-style \_Bool type,
  _where False = 0, True = 1_.
- `write_b` - Converts and writes a `int` into a signed 8-bit integer
  (a.k.a. SByte, int8_t, char).
- `write_B` - Converts and writes a `int` into an unsigned 8-bit integer
  (a.k.a. Byte, uint8_t, unsigned char).
- `write_c` - Converts and writes a `str` into an 8-bit ASCII character (a.k.a. char).
- `write_h` - Converts and writes a `int` into a signed 16-bit integer
  (a.k.a. int16_t, short).
- `write_H` - Converts and writes a `int` into an unsigned 16-bit integer
  (a.k.a. uint16_t, unsigned short, WORD).
- `write_i` - Converts and writes a `int` into a signed 32-bit integer
  (a.k.a. int32_t, int, long).
- `write_I` - Converts and writes a `int` into an unsigned 32-bit integer
  (a.k.a. uint32_t, unsigned int, unsigned long, DWORD).
- `write_q` - Converts and writes a `int` into a signed 64-bit integer
  (a.k.a. int64_t, long long).
- `write_Q` - Converts and writes a `int` into an unsigned 64-bit integer
  (a.k.a. uint32_t, unsigned long long, QWORD).
- `write_f` - Converts and writes a `float` into a 4-byte floating-point number
  (a.k.a. Single, float).
- `write_d` - Converts and writes a `float` into an 8-byte floating-point number
  (a.k.a. double).
- `write_v` - Converts and writes a `int` into a 7-bit encoded integer
  (a.k.a. varint).

## Motivation

C# `BinaryReader` and `BinaryWriter`.

## Contact

E-mail: [demberto@protonmail.com](demberto@protonmail.com)

## License

BytesIOEx is distributed under the [MIT License][license].

<!-- BADGES -->
[bandit]: https://img.shields.io/badge/security-bandit-yellow.svg
[black]: https://img.shields.io/badge/code%20style-black-black

<!-- PROJECT LINKS -->
[docs]: https://bytesioex.rtfd.io/en/latest/
[license]: https://github.com/demberto/BytesIOEx/blob/master/LICENSE
