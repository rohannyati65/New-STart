# 724. Find Pivot Index (leetcode)
# Here in this question if we use the sum function again and again we
# will get a TLE for our last test case.
# So to avoid that its better to take a random variable and assign each
# index value to this variable to get the left side sum and for right side
# for once take the sum of entire array and store its value in this
# variable and for every index value reduce that index value from this
# variable to get the right side sum for that particular index.


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
