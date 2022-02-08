# 2155. All Divisions With the Highest Score of a Binary Array (leecode)
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l=[]
        x=0
        y=nums.count(1)
        for i in range(len(nums)+1):
            if(i==len(nums)):
                if(nums[i-1]==0):
                    x+=1
                l.append(x+y)
            else:
                if(i!=0 and nums[i-1]==0):
                    x+=1
                l.append(x+y)
                if(nums[i]==1):
                    y=y-1
                
        z=max(l)
        l1=[]
        for i in range(len(l)):
            if(l[i]==z):
                l1.append(i)
        
        return(l1)