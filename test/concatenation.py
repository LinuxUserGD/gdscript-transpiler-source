#!/usr/bin/env python
import xpython.__main__
import datetime
import black
from nuitka import Version
import math
import random
import os
import sys


def test():
    print(20 + 20)
    print("hello" + "world")
    print([1, 2] + [3, 4])


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