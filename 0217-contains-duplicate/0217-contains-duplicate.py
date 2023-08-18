class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Time Complexity => O(n)
        # Space Complexity => O(n)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False