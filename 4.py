#! /usr/bin/env python3

import re
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#n = '12345'
n = '8022'
for i in range(400):
    with urllib.request.urlopen(url+n) as f:
        txt = f.read(300).decode('utf-8')
        print(txt)
        mch = re.search(r'next nothing is (\d+)', txt)
        n = mch.group(1)


