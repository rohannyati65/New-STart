# 88. Merge Sorted Array (leetcode)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        z = nums1[::-1]
        for i in range(len(z)):
            if z[0] != 0:
                break
            else:
                z.remove(0)
        nums1[:] = z[::-1]
        nums1[:] = nums1[:] + nums2[:]
        nums1.sort()
        while len(nums1) != m + n:
            nums1.append(0)
