# 2161. Partition Array According to Given Pivot (leetcode)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if pivot in nums:
            l=[pivot]*(nums.count(pivot))
        else:
            l=[pivot]
            
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]==pivot:
                pass
            
            if(nums[i]<pivot):
                l1.append(nums[i])
            
            if(nums[i]>pivot):
                l2.append(nums[i])
                
        return(l1[:]+l[:]+l2[:])