# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies (Easy)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count