# 119. Pascal's Triangle II (leetcode)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [[1]]
        a = 1
        while a != rowIndex + 1:
            a = a + 1
            l1 = [0] * a
            l2 = l[-1]

            for i in range(len(l1)):
                if i == 0:
                    l1[0] = l2[0]

                elif i == len(l1) - 1:
                    l1[i] = l2[-1]

                else:
                    l1[i] = l2[i] + l2[i - 1]

            l.append(l1)

        return l[rowIndex]
