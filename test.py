#!/urs/bin/env python

import sys
from util.csv2json import csv2json

if __name__ == "__main__":
    p = sys.argv[1]
    print(p)
    csv2json(p)