#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

import os
import sys
from PIL import Image

def main():
    print("begin convert...")
    args = sys.argv[1:]
    for infile in sys.argv[1:]:
            f, e = os.path.splitext(infile)
            outfile = f + "_new" + e
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                        w, h = im.size
                        #im.thumbnail((w//2, h//2))
                        im.thumbnail((1280, 800))
                        im.save(outfile)
                except OSError:
                    print("cannot create thumbnail for", infile)
    print("convert done.")

if __name__ == '__main__':
    main()