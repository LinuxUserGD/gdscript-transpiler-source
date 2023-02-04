#!/usr/bin/env python
import xpython.__main__
import datetime
import black
from nuitka import Version
import math
import random
import os
import sys
@export example = 99
@export_range(0, 100) example_range = 100
@export_range(0, 100, 1) example_range_step = 101
@export_range(0, 100, 1, "or_greater") example_range_step_or_greater = 102
@export color:
@export_color_no_alpha color_no_alpha:
@export_node_path(Sprite2D, Sprite3D, Control, Node) nodepath = ^ "hello"
def test():
    print(example)
    print(example_range)
    print(example_range_step)
    print(example_range_step_or_greater)
    print(color)
    print(color_no_alpha)
    print(nodepath)
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
