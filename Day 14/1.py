# 78. Subsets (leetcode)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        k=len(nums)
        while(k!=0):
            b=list(map(list,itertools.combinations(nums,k)))
            k=k-1
            for i in b:
                i.sort()
                if i not in l:
                    l.append(i)
        return(l)