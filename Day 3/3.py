# 26. Remove Duplicates from Sorted Array (leetcode)
# 2 Methods (Both Accepted)

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
