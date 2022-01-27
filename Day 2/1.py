# 1480. Running Sum of 1d Array(Leetcode)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            l.append(sum(nums[: i + 1]))
        return l
