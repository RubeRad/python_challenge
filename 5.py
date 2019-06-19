#! /usr/bin/env python3

import pickle
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
out = pickle.load(urllib.request.urlopen(url))
#print(out)

for row in out:
    for grp in row:
        for i in range(grp[1]):
            print(grp[0], end='')
    print('')
