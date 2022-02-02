#  (leetcode)

# 1st Attempt (TLE)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = []
        a = len(p)
        for i in range(len(s) - a + 1):
            x = s[i : i + a]
            y = 0
            for j in x:
                if len(x) == a and x.count(j) == p.count(j):
                    y = 1
                else:
                    y = 0
                    break
            if y == 1:
                l.append(i)
        return l


# 2nd Attempt (TLE)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = []
        a = len(p)
        lst = [i for i in p]
        lst.sort()

        for i in range(len(s) - a + 1):
            x = [j for j in s[i : i + a]]
            x.sort()
            if lst == x:
                l.append(i)
        return l


# 3rd Attempt
