class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charset = set()
        l = 0 
        result = 0

        # right pointer will the changing as we move the window

        for r in range(len(s)):
            print(r)
            while s[r] in charset:
                #if char at right pointer already in the set
                #update the left pointer =>
                # shrink the window 
                # and also remove the character at l from set
                charset.remove(s[l])
                l = l+1 
            charset.add(s[r])
            result = max(result, r-l+1)
        return result
