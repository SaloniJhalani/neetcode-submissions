class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
        
        buckets = [[] for _ in range(0, len(nums)+1)]
        # print(dic)
        # print(buckets)

        for key, value in dic.items():
            buckets[value].append(key)

        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                output.append(val)
                if len(output) == k:
                    return output

        