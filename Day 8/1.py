# 80. Remove Duplicates from Sorted Array II (leetcode)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=list(set(nums))
        for i in x:
            k=0
            a=nums.count(i)
            if(a>2):
                while(a!=2):
                    nums.remove(i)
                    a=a-1
        return(len(nums))