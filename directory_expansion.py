from directory import Directory
from bucket import Bucket
from hash_function import Hash

from lsb_to_index import LsbToIndex
lsbtoindex = LsbToIndex()
hash = Hash()
dir = Directory()
class DirectoryExpansion:
    def rehashKeys(self, old_idx, new_idx, key):
        for i,x in enumerate(dir.l[old_idx].l):
            key_binary_format = hash.hashFunction(key)
            idx = lsbtoindex.lsbToIndex(key_binary_format)
            if idx != old_idx:
                dir.l[new_idx].l.append(dir.l[old_idx].l.pop(i))
        key_binary_format = hash.hashFunction(key)
        idx = lsbtoindex.lsbToIndex(key_binary_format)
        if idx != old_idx:
            dir.l[new_idx].l.append(key)
        else:
            dir.l[old_idx].l.append(key)
    def directoryExpansion(self,idx,key):
        dir.gd = dir.gd + 1
        dir.l[idx].ld = dir.l[idx].ld + 1
        i = 0
        while len(dir.l) != pow(2,dir.gd):
            dir.l.append(dir.l[i])
            i = i + 1
        new_buck = Bucket(ld=dir.l[idx].ld)
        print("Collision At index :",idx)
        new_index = idx + pow(2, dir.gd-1)
        print("New index generated: ",new_index)
        dir.l[new_index] = new_buck
        self.rehashKeys(idx,new_index,key)