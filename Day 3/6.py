# 7. Reverse Integer (leetcode)
class Solution:
    def reverse(self, x: int) -> int:
        if (-2147483648) <= x <= (2147483647):
            if x > 0:
                y = str(x)
                z = y[::-1]
                w = int(z)
                if (-2147483648) <= w <= (2147483647):
                    return w
                else:
                    return 0
            else:
                x = x * (-1)
                y = str(x)
                # z=y[1:]
                w = y[::-1]
                # print(w)
                v = int(w)
                a = v * (-1)
                if (-2147483648) <= a <= (2147483647):
                    return a
                else:
                    return 0
        else:
            return 0
