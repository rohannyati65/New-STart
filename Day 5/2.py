# 1137. N-th Tribonacci Number (leetcode)
class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]
        if n == 0:
            return l[0]
        if n == 1:
            return l[1]
        if n == 2:
            return l[2]

        while len(l) != n + 1:
            x = l[-1] + l[-2] + l[-3]
            l.append(x)
        return l[-1]
