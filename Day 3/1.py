# 122. Best Time to Buy and Sell Stock II (leetcode)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        y = prices[0]
        a = 0
        for i in range(1, len(prices)):
            x = prices[i]
            if prices[i - 1] > prices[i]:
                p = p + a
                y = prices[i]
                a = 0

            else:
                y = min(y, x)

            z = x - y
            a = max(a, z)

            if i == len(prices) - 1:
                p = p + a

        return p
