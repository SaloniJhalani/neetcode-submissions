class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_without_zero = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero = count_zero + 1

            if (count_zero == 1) & (num == 0):
                product_without_zero = product
            
            elif (count_zero == 1) & (num != 0):
                product_without_zero = product_without_zero * num
            
            else:
                product = product * num

        output = []
        for i, num in enumerate(nums):
            if count_zero == 0:
                output.append(product // num)
            elif count_zero == 1:
                if num==0:
                    output.append(product_without_zero)
                else:
                    output.append(0)
            else:
                output.append(0)
        
        return output
        