# 1672. Richest Customer Wealth (leetcode)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = [0]
        for i in accounts:
            l.append(sum(i))
        return max(l)
