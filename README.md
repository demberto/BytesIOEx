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

## ⏬ Installation

BytesIOEx requires Python 3.6+, it may run on older version as well but I have
not tested it.

```
pip install --upgrade bytesioex
```

## 📜 Documentation

Docs are available on [ReadTheDocs][docs].

## 🚀 Roadmap

- [ ] Ensure full coverage.
- [ ] Add `wchar` (UTF-16 character) support.
- [ ] Support for different byte orders.

## ❕ Motivation

C# `BinaryReader` and `BinaryWriter`.

## 📧 Contact

E-mail: demberto@protonmail.com

## © License

BytesIOEx is distributed under the [MIT License][license].

<!-- BADGES -->
[bandit]: https://img.shields.io/badge/security-bandit-yellow.svg
[black]: https://img.shields.io/badge/code%20style-black-black

<!-- PROJECT LINKS -->
[docs]: https://bytesioex.rtfd.io/en/latest/
[license]: https://github.com/demberto/BytesIOEx/blob/master/LICENSE
