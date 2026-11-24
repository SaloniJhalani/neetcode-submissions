class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d1 = {}
            d2 = {}
            for num in s:
                if num in d1:
                    d1[num] +=1
                else:
                    d1[num] = 1
            
            for num in t:
                if num in d2:
                    d2[num] +=1
                else:
                    d2[num] = 1

            return d1==d2
            
        