# 746. Min Cost Climbing Stairs (leetcode)
# 1st attempt (wrong ans (263/283))
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a=len(cost)
        if(a<2):
            return(sum(cost))
        
        x=0
        if(a==2):
            s1=min(cost[-1],cost[-2])
        else:
            s1=min(cost[-1]+cost[-3],cost[-2])
            
        while(x<a-3):
            s1=s1+cost[x]
            if (x==a-1-3) or (x==a-2-3):
                x=a
            
            elif(cost[x+1]<cost[x+2]):
                x=x+1
                
            elif(cost[x+1]>cost[x+2]):
                x=x+2
            
            elif(cost[x+1]==cost[x+2]):
                x=x+2
                
        y=1
        b=len(cost[y:])
        if(b==2):
            s2=min(cost[-1],cost[-2])
        else:
            if(b==1):
                s2=cost[-1]
            else:
                s2=min(cost[-1]+cost[-3],cost[-2]+cost[-4],cost[-2]+cost[-3])
            
        while(y<b-3):
            s2=s2+cost[y]
            if (y==b-1-3) or (y==b-2-3):
                y=b
            
            elif(cost[y+1]<cost[y+2]):
                y=y+1
                
            elif(cost[y+1]>cost[y+2]):
                y=y+2
                
            elif(cost[y+1]==cost[y+2]):
                y=y+2
        
        return(min(s1,s2))

# 2nd attempt(correct)
