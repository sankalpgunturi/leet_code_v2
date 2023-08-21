class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [None] * n
        prefix, postfix = 1, 1
        
        for i, num in enumerate(nums):
            output[i] = prefix
            prefix = prefix * num
        
        for i in range(n-1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]

        return output
