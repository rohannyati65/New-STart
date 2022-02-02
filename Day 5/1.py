# 438. Find All Anagrams in a String (leetcode)

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


# 3rd Attempt (Accepted)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        pCount = {}
        sCount = {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        if pCount == sCount:
            res = [0]
        else:
            res = []

        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l = l + 1
            if sCount == pCount:
                res.append(l)

        return res
