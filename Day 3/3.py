# 26. Remove Duplicates from Sorted Array (leetcode)
# 2 Methods (Both Accepted)
#Here in the first methode we have a Time Complexity of O(n^2) while in 2nd case we have it as O(n).
# 1st
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            while nums.count(i) != 1:
                nums.remove(i)
        return len(nums)


# 2nd (Better)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        while a != len(nums):
            if nums.count(nums[a]) != 1:
                nums.remove(nums[a])
            else:
                a += 1
        return len(nums)
