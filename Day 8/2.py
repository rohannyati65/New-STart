# 2164. Sort Even and Odd Indices Independently (leetcode)
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(len(nums)):
            if(i%2==0):
                e.append(nums[i])
            else:
                o.append(nums[i])
        
        e.sort()
        o.sort()
        o=o[::-1]
        
        l=[0]*len(nums)
        x=0
        y=0
        z=0
        for i in range(len(nums)):
            if(z==0):
                l[i]=e[x]
                x+=1
                z=1
            
            elif(z==1):
                l[i]=o[y]
                y+=1
                z=0
        
        return(l)