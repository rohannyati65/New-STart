# 2160. Minimum Sum of Four Digit Number After Splitting Digits (leetcode)
class Solution:
    def minimumSum(self, num: int) -> int:
        l=[]
        for i in str(num):
            if(i=="0"):
                pass
            else:
                l.append(int(i))
        l.sort()
        x=""
        for i in range(len(l)):
            x=x+str(l[i])
        
        if(len(x)==1):
            return(int(x))
        
        if(len(x)==0):
            return(0)
        
        a=x[:(len(x)//2)]
        b=x[len(x)//2:]
        
        num1=""
        num2=""
        
        if(len(a)>1):
            if(len(a)%2==0):
                num1=num1+a[:len(a)//2]
                num2=num2+a[len(a)//2:]
            else:
                num1=num1+a[:(len(a)//2)+1]
                num2=num2+a[(len(a)//2)+1:]
            
        if(len(a)==1):
            num1=num1+a[0]
            
        if(len(b)>1):
            if(len(b)%2==0):
                num2=num2+b[:len(b)//2]
                num1=num1+b[len(b)//2:]
            else:
                num2=num2+b[:(len(b)//2)+1]
                num1=num1+b[(len(b)//2)+1:]
        
        if(len(b)==1):
            num2=num2+b[-1]
            
        #print(num1,num2,a,b)
        return(int(num1)+int(num2))