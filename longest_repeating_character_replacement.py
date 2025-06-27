class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = {}

        result = 0

        l = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0) 

            while (r-l+1) - max(hashmap.values()) > k:
                hashmap[s[l]] = hashmap[s[l]] -1
                l = l+1 

            result = max(result, r - l + 1)
        return result
