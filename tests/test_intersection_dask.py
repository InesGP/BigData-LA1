import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import intersection_dask

def test_intersection_dask():
    a = intersection_dask(os.path.join('.', 'data', 'frenepublicinjection2016.csv'), os.path.join('.', 'data', 'frenepublicinjection2015.csv'))
    try:
        out = open(os.path.join('tests', 'intersection.txt'),"r").read()
        assert(a == out)
    except:
        try:
            out = open(os.path.join('tests', 'intersection.txt'),"r", encoding="ISO-8859-1").read()
            assert(a == out)
        except:
            try:
                out = open(os.path.join('tests', 'intersection.txt'),"r", encoding="utf-8").read()
                assert(a == out)
            except:
                out = open(os.path.join('tests', 'intersection.txt'),"r", encoding="latin1").read()
                assert(a == out)
