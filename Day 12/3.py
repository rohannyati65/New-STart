# 2150. Find All Lonely Numbers in the Array (leetcode)

# Here in this ques we don't have to think much and just have to apply basic 
# understanding of concepts and follow the ques as it is told .

# So first we sort the array to make things easier and save our time from 
# again and again checking for conditions in our array .

# Then we use the concept of sliding window , to check for 3 array values at 
# a time the current one and compare it with the previous and next value at 
# once and follow the conditions told in the ques.

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if(len(nums)<=1):
            return(nums)
        
        nums.sort()
        l=[]
        for i in range(len(nums)):
            if(i==0):
                if (nums[i]!=nums[i+1]) and (nums[i+1]!=(nums[i]+1)):
                    l.append(nums[i])
                
            elif(i==len(nums)-1):
                if (nums[i]!=nums[i-1]) and (nums[i-1]!=(nums[i]-1)):
                    l.append(nums[i])
            
            else:
                if (nums[i]!=nums[i+1]) and (nums[i+1]!=(nums[i]+1)) and (nums[i]!=nums[i-1]) and (nums[i-1]!=(nums[i]-1)):
                    l.append(nums[i])
        
        return(l)