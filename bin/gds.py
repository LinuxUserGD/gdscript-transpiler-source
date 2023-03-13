#!/usr/bin/env python
import os
import sys


def _init():
    gds = {}
    sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(__file__), "..")))
    import gds.__main__

    gds.__main__._init()
    sys.exit()


if __name__ == "__main__":
    _init()
