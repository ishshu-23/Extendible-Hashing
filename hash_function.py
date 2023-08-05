from findsum import FindSum
from directory import Directory
dir = Directory()

class Hash:
    def hashFunction(self, key):
        obj = FindSum()
        key_ascii_sum = obj.findSum(key)
        # print("The Sum of Ascii Value of key:",key,"is ",key_ascii_sum)
        s = bin(key_ascii_sum)
        # print("Key Binary Format: ", s)
        x = ""
        for i in range(dir.gd):
            if s[-1-i] == 'b':
                break
            x = (s[-1-i]) + x
        while len(x) != dir.gd:
            x = '0' + x
        # print("Binary Form of Key: ", x)
        return x

# hash = Hash()
# print(hash.hashFunction("Saquib"))