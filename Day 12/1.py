# 2148. Count Elements With Strictly Smaller and Greater Elements (leetcode)
class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        x=len(nums)
        y=nums.count(nums[0])
        z=0
        if(nums[0]!=nums[-1]):
            z+=nums.count(nums[-1])
        
        return(x-(y+z))