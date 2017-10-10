#!/usr/bin/python
import urllib.request
import sys
import time

def parseFile(path):
    urls = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line[:4] == 'http':
                urls.append(line)
    return urls


def download(arr):
    for url in arr:
        try:
            start = time.time()
            file_name = url.split('/')[-1]
            urllib.request.urlretrieve(url, file_name)
            t = time.time()
            print(u" \u2713  " + "%s [%.2f s]" % (file_name, t - start))
        except:
            print("!!  Failed to download from " + url)


if __name__ == '__main__':
    # print('Hello World')
    p = sys.argv[1]
    # print(p)
    begin = time.time()
    download(parseFile(p))
    print("Total time used: %.2f s\n" % (time.time() - begin))
