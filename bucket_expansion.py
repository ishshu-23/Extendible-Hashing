from bucket import Bucket
from directory import Directory
from hash_function import Hash
from lsb_to_index import LsbToIndex
lsb = LsbToIndex()
hash = Hash()
dir = Directory()
# buket_obj = dir.l[i].ld
# dir.l[0] = Bucket(ld=2)
# buc_obj = dir.l[0]    
# buc_obj.l.append("H")
# buc_obj.l.append("HH")
# buc_obj.l.append("HHH")

class BucketExpansion:
    
    def rehashKeys(self, old_idx, new_idx, key, ld):
        for i, x in enumerate(dir.l[old_idx].l):
            key_binary_format = hash.hashFunction(x)

            idx = lsb.lsbToIndex(key_binary_format)
            if idx != old_idx:
                dir.l[new_idx].l.append(dir.l[old_idx].l.pop(i))
        # print("Key is :", key)
        key_binary_format = hash.hashFunction(key)
        # print("Binary Format of Key is: ", key_binary_format)
        idx = lsb.lsbToIndex(key_binary_format)
        # print("Idx of key: ", idx)
        if idx != old_idx:
            dir.l[new_idx].l.append(key)
        else:
            dir.l[old_idx].l.append(key)

    def bucketExpansion(self, i, key):
        obj = dir.l[i]
        i = dir.l.index(obj)
        new_index = i + pow(2,dir.l[i].ld)
        # print("New Index is :",new_index)
        dir.l[i].ld = dir.l[i].ld + 1
        new_buck = Bucket(ld=dir.l[i].ld)
        dir.l[new_index] = new_buck
        self.rehashKeys(i, new_index, key, dir.l[i].ld)

# bucket_expansion = BucketExpansion()
# print(dir.l)
# bucket_expansion.bucketExpansion(0, "HHHH")
# print(dir.l)
# for x in dir.l:
# if x != None:
# print("Bucket Object: ",end=" ")
# for y in x.l:
# print(y,end=" ")