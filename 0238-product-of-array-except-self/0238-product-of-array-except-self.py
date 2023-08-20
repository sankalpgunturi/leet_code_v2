class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix, output = [None] * n, [None] * n, [None] * n

        prefix[0] = nums[0]
        postfix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        for i in range(n):
            if i <= 0:
                a = 1
            else:
                a = prefix[i-1]
            if i >= n-1:
                b = 1
            else:
                b = postfix[i+1]
            
            output[i] = a * b
            
        return output
