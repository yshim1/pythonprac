class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spoint, tpoint = 0, 0

        while spoint < len(s) and tpoint < len(t):
            if s[spoint] == t[tpoint]:
                spoint += 1
            tpoint += 1
        return spoint == len(s)