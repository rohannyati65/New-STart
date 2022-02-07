# 2165. Smallest Value of the Rearranged Number (leetcode)
class Solution:
    def smallestNumber(self, num: int) -> int:
        x=str(num)
        l=[i for i in x]
        if "-" in l:
            l1=["-"]
            l.remove("-")
            for i in range(len(l)):
                l[i]=int(l[i])
            l.sort(reverse=True)
            l1[:]=l1[:]+l[:]
            y=""
            for i in l1:
                y=y+str(i)
            return(int(y))
            
        else:
            l1=[]
            l=[int(i) for i in x]
            l.sort()
            for i in range(len(l)):
                if(l[i]==0):
                    l1.append(0)
                else:
                    l1.insert(0,l[i])
                    if(i!=len(l)-1):
                        l1[:]=l1[:]+l[i+1:]
                    break
            y=""
            for i in l1:
                y=y+str(i)
            return(int(y))
            
                    
            