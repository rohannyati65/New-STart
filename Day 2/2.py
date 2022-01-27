# 724. Find Pivot Index (leetcode)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = sum(nums)
        x = 0
        for i in range(len(nums)):
            a = a - nums[i]
            # print(x,a)
            if i == 0:
                if 0 == a:
                    return i

            elif i != (len(nums) - 1):
                if x == a:
                    return i

            elif i == (len(nums) - 1):
                if x == 0:
                    return i

            x = x + nums[i]

        return -1
