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
    # Non-string keys are valid.
    print({12: "world"}[12])
    contents = {
        0: "zero",
        0.0: "zero point zero",
        None: "null",
        false: "false",
        []: "empty array",
        i(): "zero Vector2i",
        15: {
            22: {
                4: ["nesting", "arrays"],
            },
        },
    }
    print(contents[0.0])
    # Making sure declaration order doesn't affect things...
    print(
        {
            0.0: "zero point zero",
            0: "zero",
            None: "null",
            false: "false",
            []: "empty array",
        }[0]
    )
    print(
        {
            0.0: "zero point zero",
            0: "zero",
            None: "null",
            false: "false",
            []: "empty array",
        }[0.0]
    )
    print(contents[None])
    print(contents[false])
    print(contents[[]])
    print(contents[Vector2i()])
    print(contents[15])
    print(contents[15][22])
    print(contents[15][22][4])
    print(contents[15][22][4][0])
    print(contents[15][22][4][1])
    # Currently fails with "invalid get index 'hello' on base Dictionary".
    # Both syntaxes are valid however.
    # print({ "hello": "world"}[ "hello"])
    # print({ "hello": "world"}.hello)


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
