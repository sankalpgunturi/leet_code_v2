class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                res = m
                break
            if nums[l] <= nums[r]:
                if target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
                continue
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return res
