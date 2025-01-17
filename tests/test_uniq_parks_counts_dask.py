import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import uniq_parks_counts_dask

def test_uniq_parks_count_dask():
    a = uniq_parks_counts_dask(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    try:
        out = open(os.path.join('tests', 'list_parks_count.txt'),"r").read()
        assert(a == out)
    except:
        try:
            out = open(os.path.join('tests', 'list_parks_count.txt'),"r", encoding="ISO-8859-1").read()
            assert(a == out)
        except:
            try:
                out = open(os.path.join('tests', 'list_parks_count.txt'),"r", encoding="utf-8").read()
                assert(a == out)
            except:
                out = open(os.path.join('tests', 'list_parks_count.txt'),"r", encoding="latin1").read()
                assert(a == out)
