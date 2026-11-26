class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dic = {}
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] +=1
            key = tuple(count)
            if key not in dic:
                dic[key] = []
            dic[key].append(s)

        for key, value in dic.items():
            output.append(value)
      
        return output
