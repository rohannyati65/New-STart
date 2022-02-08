# 258. Add Digits (leetcode)
class Solution:
    def addDigits(self, num: int) -> int:
        if(len(str(num))==1):
            return(num)
        
        x=0
        for i in str(num):
            x=x+int(i)

        return(Solution().addDigits(x))