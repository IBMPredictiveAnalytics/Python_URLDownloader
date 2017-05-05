# encoding=utf-8

import sys
import urllib2

if len(sys.argv) > 1 and sys.argv[1] == "-test":
    url = sys.argv[2]
    filePath = sys.argv[3]
else:
    url = '%%url%%'
    filePath = '%%path%%'

if not url or not filePath:
    raise "must specify values for both URL and file path"

req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
file = open(filePath, "wb")
file.write(content)
file.close()
