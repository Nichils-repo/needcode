class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new = set(nums)
        longest = 0

        for i in new:
            if(i -1) not in new:
                length = 1
                while (i + length) in new:
                    length = length + 1
                longest = max(longest,length)
        return longest
