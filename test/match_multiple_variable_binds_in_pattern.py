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
    match [1, 2, 3]:
        case [var a, b, c]:
            print(a == 1)
            print(b == 2)
            print(c == 3)
def left(s, amount):
    return s[:amount]
def right(s, amount):
    return s[len(s)-amount:]
def resize(arr, size):
    if len(arr)==0:
        arr.append(None)
    arr *= size
    return arr
if __name__=="__main__":
    _init()
