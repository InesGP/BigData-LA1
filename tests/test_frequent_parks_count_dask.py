import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count_dask

def test_frequent_parks_count_dask():
    a = frequent_parks_count_dask("./data/frenepublicinjection2016.csv")
    assert(a == open("tests/frequent.txt","r").read())