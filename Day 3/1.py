# 122. Best Time to Buy and Sell Stock II (leetcode)

# Here in this solution we try to find different pivot points and as per
# them we keep on changing the value for our y variable (i.e. the point
# in time where we should buy our stocks at lowest price).

# Till we find a pivot point (condition where the previous value was
# bigger then the current value) we keep on finding the max value for our
# price till that time and store it in a temporary variable "a" for the
# time being , and then keep on adding this value of "a" to "p" as soon
# as we hit a pivot point to get the max value of prices .


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
