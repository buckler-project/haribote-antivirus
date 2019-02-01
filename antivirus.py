import sys
from buckler import Buckler
from pprint import pprint


with open(sys.argv[1], 'rb') as f: 
    body = f.read()
    buckler = Buckler()
    has_hit = buckler.scan(body)

    if has_hit:
        print("hit")
        pprint(buckler.hits())

