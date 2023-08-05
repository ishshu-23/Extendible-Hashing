from directory import Directory
from hash_function import Hash
from lsb_to_index import LsbToIndex
from key_insertion import KeyInsertion

keyinsert_obj = KeyInsertion()
dir = Directory()
hash = Hash()
lsb_to_index_obj = LsbToIndex() 

with open("test.c","r") as f:
    size = 10
    f_str = f.read(size)
    print(f_str)

    while len(f_str) != 0:
        if len(f_str) < size:
            spaces = " " * (size - len(f_str))
            f_str = f_str + spaces

        lsb = hash.hashFunction(f_str)
        i = lsb_to_index_obj.lsbToIndex(lsb)
        keyinsert_obj.keyInsertion(i,f_str)
        f_str = f.read(size)