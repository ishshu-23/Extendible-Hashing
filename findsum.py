class FindSum:
    def findSum(self,s1):
        sum = 0
        for x in s1:
            sum += ord(x)
        return sum