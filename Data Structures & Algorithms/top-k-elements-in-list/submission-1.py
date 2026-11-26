class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1

            if num not in output:
                if (len(output) < k):
                    output.append(num)
                else :
                    min_count = dic[num]
                    min_count_index = -1
                    for i,o in enumerate(output):
                        if dic[o] < min_count:
                            min_count_index = i
                            min_count = dic[o]
                    if min_count_index >=0 :
                        output[min_count_index] = num
            # print(output)

        return output

        