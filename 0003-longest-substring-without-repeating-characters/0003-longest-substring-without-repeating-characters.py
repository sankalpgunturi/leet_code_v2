class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        output = 0

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            output = max(output, r - l + 1)
        return output