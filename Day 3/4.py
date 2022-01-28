# 118. Pascal's Triangle (leetcode)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        l = [[1]]
        a = 1
        while a != numRows:
            a = a + 1
            l2 = l[-1]
            l1 = [0] * a
            for i in range(len(l1)):
                if i == 0:
                    l1[i] = l2[i]

                elif i == len(l1) - 1:
                    l1[i] = l2[-1]

                else:
                    l1[i] = l2[i] + l2[i - 1]

            l.append(l1)
        return l
