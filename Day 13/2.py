# 2144. Minimum Cost of Buying Candies With Discount (leetcode)
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        s=0
        while(len(cost)!=0):
            if(len(cost)<2):
                s=s+cost[-1]
                cost.remove(cost[-1])
            else:
                s=s+cost[-1]
                cost.remove(cost[-1])
                s=s+cost[-1]
                cost.remove(cost[-1])
                if(len(cost)>0):
                    cost.remove(cost[-1])
        return(s)