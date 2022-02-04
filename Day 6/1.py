# 525. Contiguous Array (leetcode)
# 1st Attempt(Wrong)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l != r:
            if nums[l : r + 1].count(0) == nums[l : r + 1].count(1):
                return r - l + 1

            elif nums[l : r + 1].count(0) > nums[l : r + 1].count(1):
                if nums[l] == 0:
                    l = l + 1

                elif nums[r] == 0:
                    r = r - 1

                else:
                    l = l + 1

            elif nums[l : r + 1].count(1) > nums[l : r + 1].count(0):
                if nums[l] == 1:
                    l = l + 1

                elif nums[r] == 1:
                    r = r - 1

                else:
                    l = l + 1
            # print(l,r,nums[l],nums[r],nums[l:r+1])

        return 0


# 2nd Attempt(Accepted)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = 0
        d = {}
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                s = s - 1

            if nums[i] == 1:
                s = s + 1

            if s == 0:
                l = i + 1

            if s in d:
                l = max(l, i - d[s])

            else:
                d[s] = i

        return l


# 3rd Easy One To Understand
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        hash = {}
        count = 0
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1  # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
                count += 1

            if count == 0:
                # if count is 0, we have a new subarray with length+1
                max_length = i + 1
            if count in hash:
                max_length = max(max_length, i - hash[count])
            else:
                hash[count] = i
        return max_length
