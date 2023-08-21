class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                count = 1
                while (n + 1) in numSet:
                    count += 1
                    n += 1
                longest = max(count, longest)
        return longest


