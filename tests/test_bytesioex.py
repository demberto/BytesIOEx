"""Tests `BytesIOEx` class."""

import math
import random
from typing import Callable

import pytest

from bytesioex import (
    Bool,
    Byte,
    BytesIOEx,
    Double,
    Float,
    Int,
    Long,
    SByte,
    Short,
    UInt,
    ULong,
    UShort,
)

INT8_MIN = -(2**7)
INT8_MAX = (2**7) - 1
UINT8_MAX = (2**8) - 1

INT16_MIN = -(2**15)
INT16_MAX = (2**15) - 1
UINT16_MAX = (2**16) - 1

INT32_MIN = -(2**31)
INT32_MAX = (2**31) - 1
UINT32_MAX = (2**32) - 1

INT64_MIN = -(2**63)
INT64_MAX = (2**63) - 1
UINT64_MAX = (2**64) - 1

UINT8_MIN = UINT16_MIN = UINT32_MIN = UINT64_MIN = 0

CONVERTER = {
    "B": Byte,
    "b": SByte,
    "H": UShort,
    "h": Short,
    "I": UInt,
    "i": Int,
    "f": Float,
    "d": Double,
    "q": Long,
    "Q": ULong,
}


@pytest.mark.parametrize(
    "min_, max_, fmt",
    [
        (UINT8_MIN, UINT8_MAX, "B"),
        (INT8_MIN, INT8_MAX, "b"),
        (UINT16_MIN, UINT16_MAX, "H"),
        (INT16_MIN, INT16_MAX, "h"),
        (UINT32_MIN, UINT32_MAX, "I"),
        (INT32_MIN, INT32_MAX, "i"),
        (UINT64_MIN, UINT64_MAX, "Q"),
        (INT64_MIN, INT64_MAX, "q"),
    ],
)
def test_read_integer_types(min_: int, max_: int, fmt: str):
    """Tests `read_{B,b,H,h,I,i,Q,q}` and `write_{B,b,H,h,I,i,Q,q}`."""
    num = random.randint(min_, max_)
    converter = CONVERTER[fmt]
    with BytesIOEx(converter.pack(num)) as b:
        read_func: Callable[[], int] = getattr(b, "read_" + fmt)
        assert read_func() == num
        b.seek(0)
        write_func: Callable[[int], int] = getattr(b, "write_" + fmt)
        _ = write_func(num)
        b.seek(0)
        assert read_func() == num


def test_char():
    """Tests `read_c` and `write_c`."""
    letter = chr(random.randrange(65, 126))
    with BytesIOEx(letter.encode("ascii")) as b:
        b.write_c(letter)
        b.seek(0)
        assert b.read_c() == letter


def test_bool():
    """Tests `read_bool` and `write_bool`."""
    with BytesIOEx(Bool.pack(True)) as b:
        b.write_bool(False)
        b.seek(0)
        assert not b.read_bool()


def test_double():
    """Tests `read_d` and `write_d`."""
    dbl = random.random()
    with BytesIOEx(Double.pack(dbl)) as b:
        # A 64-bit floating point integer has about 16 digits of precision
        assert math.isclose(b.read_d(), dbl, rel_tol=1e-16)
        b.write_d(dbl)
        b.seek(1)


def test_float():
    """Tests `read_f` and `write_f`."""
    flt = random.random()
    with BytesIOEx(Float.pack(flt)) as b:
        # A 32-bit floating point integer has about 7 digits of precision
        assert math.isclose(b.read_f(), flt, rel_tol=1e-7)
        b.write_f(flt)
        b.seek(1)


def test_varint():
    """Tests `read_v` and `write_v`."""
    bignum = random.randint(2**8, 2**32)
    with BytesIOEx() as b:
        b.write_v(bignum)
        b.seek(0)
        assert b.read_v() == bignum
