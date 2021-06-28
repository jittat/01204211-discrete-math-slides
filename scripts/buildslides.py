#!/usr/bin/env python
import sys

from buildutils import build

template = "slides.template"

def main():
    if len(sys.argv) < 2:
        print("Usage: buildslides.py [filename.tex]")
        quit()
    fname = sys.argv[1]
    if fname.endswith('.'):
        fname = fname + 'tex'
    build(fname, "slides.template", "%s.slides.tex")

if __name__ == '__main__':
    main()
