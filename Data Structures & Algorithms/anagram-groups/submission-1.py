class Solution:        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for s in strs:
            flag = 0
            for t in result:
                if self.isAnagram(s, t[0]):
                    t.append(s)
                    flag = 1
                    break
            if flag == 0:
                result.append([s])

        return result
    

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
        






