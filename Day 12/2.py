# 2149. Rearrange Array Elements by Sign (leetcode)
# 1st Method (Accepted)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in nums:
            if "-" in str(i):
                l2.append(i)
            else:
                l1.append(i)
        
        if(len(l1)!=len(l2)):
            return([])
        a=1
        b=0
        while(a<len(nums)):
            l1.insert(a,l2[b])
            b+=1
            a+=2
        
        return(l1)

# 2nd Method (Accepted * 100 Times Better)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1=[0]*len(nums)
        a=1
        b=0
        for i in nums:
            if "-" in str(i):
                l1[a]=i
                a+=2
            else:
                l1[b]=i
                b+=2
        
        return(l1)