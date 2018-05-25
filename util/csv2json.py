#!/usr/bin/env python

import json
import sys
from .splitLine import splitLine # it works


def csv2json(path):
    counter = 0
    target = open(path+'.json', 'w')
    target.write('[\n')
    header = []
    with open(path) as f:
        for line in f:
            line = line[:-1]
            if counter > 1:
                fields = splitLine(line)
                d = {}
                if len(fields) != len(header):
                    print("error happens to match to header")
                    print(line)
                for i in range(len(fields)):
                    d[header[i]] = fields[i]
                target.write(',\n' + json.dumps(d))
            else:
                if counter == 0:
                    header = splitLine(line)
                if counter == 1:
                    fields = splitLine(line)
                    d = {}
                    if len(fields) != len(header):
                        print("error happens to match to header")
                        print(line)
                    for i in range(len(fields)):
                        d[header[i]] = fields[i]
                    target.write( json.dumps(d))
            counter += 1
        target.write('\n]')
    print("Convertion finished!")


if __name__ == "__main__":
    p = sys.argv[1]
    print(p)
    csv2json(p)