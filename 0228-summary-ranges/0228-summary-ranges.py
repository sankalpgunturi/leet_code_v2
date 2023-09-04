class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        beat = -1
        i = 0
        while i < len(nums):
            start = end = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == (end + 1):
                    end = nums[j]
                    beat = j
            i = max(beat+1, i+1)
            if start != end:
                output.append(str(start) + "->" + str(end))
            else:
                output.append(str(start))
        return output