#!/usr/bin/env python
import xpython.__main__
import datetime
import black
from nuitka import Version
import math
import random
import os
import sys
# https://github.com/godotengine/godot/issues/56751
def test():
    x = "local"
    lambda = func(param = x):
        print(param)
    lambda.call()
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