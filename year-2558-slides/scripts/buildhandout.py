#!/usr/bin/env python
import sys

from buildutils import build

def main():
    if len(sys.argv) < 2:
        print "Usage: buildhandout.py [filename.tex]"
        quit()

    fname = sys.argv[1]
    if fname.endswith('.'):
        fname = fname + 'tex'
    build(fname, "handout.template", "%s.handout.tex")

if __name__ == '__main__':
    main()
