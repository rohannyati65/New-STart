# 283. Move Zeroes (Leetcode)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=len(nums)
        x=0
        while(x!=len(nums)):
            if nums[x]==0:
                nums.remove(0)
            else:
                x+=1
        
        b=[0]*(a-len(nums))
        nums[:]=nums[:]+b[:]
        