class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mp = {}
        for i in s:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        for i in t:
            if mp.get(i) == None or mp.get(i) == 0:
                return False
            else:
                mp[i] -= 1

        return True
        