#!/usr/bin/env python
import xpython.__main__
import datetime
import black
from nuitka import Version
import math
import random
import os
import sys


def example(_number, _number2=5, number3=10):
    return number3


def test():
    print(example(3))


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[len(s) - amount :]


def resize(arr, size):
    if len(arr) == 0:
        arr.append(None)
    arr *= size
    return arr


if __name__ == "__main__":
    _init()