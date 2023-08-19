class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for p, q in enumerate(nums):
            change = target - q
            if change in myMap:
                return [myMap[change], p]
            myMap[q] = p
