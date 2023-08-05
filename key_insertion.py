from directory import Directory
from bucket import Bucket
from bucket_expansion import BucketExpansion
from directory_expansion import DirectoryExpansion
directory_expansion_obj = DirectoryExpansion()
bucket_expansion_obj = BucketExpansion()
dir = Directory()
class KeyInsertion:
    def keyInsertion(self,i, key):
        if dir.l[i] == None:
            dir.l[i] = Bucket()
            dir.l[i].l.append(key)
        else:
            buc_obj = dir.l[i]
            if len(buc_obj.l) < buc_obj.size:
                buc_obj.l.append(key)
            else:
                #collsion resolution
                # print("Collsion Occured")
                if dir.gd > buc_obj.ld:
                    print("GD = ",dir.gd,"LD = ",buc_obj.ld)
                    print("Bucket Before Expansion:")
                    print(dir.l)
                    bucket_expansion_obj.bucketExpansion(i,key)
                    print("Bucket After Expansion:")
                    print(dir.l)
                else:
                    print("GD = ",dir.gd,"LD = ",buc_obj.ld)
                    print("Directory Before Expansion:")
                    print(dir.l)
                    directory_expansion_obj.directoryExpansion(i,key)

                    print("Directory After Expansion:")
                    print(dir.l)
# insert = KeyInsertion()
# insert.keyInsertion(1, "Saquib1")
# insert.keyInsertion(1, "Saquib2")
# insert.keyInsertion(1, "Saquib3")
# insert.keyInsertion(0, "Saquib4")
# for x in dir.l:
    # if x != None:
        # print(x.l)