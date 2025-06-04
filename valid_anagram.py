# using hashmaps 
# time complexity = O(s+t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #base condition
        if len(s) != len(t):
            return False

        countS , countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # ,0 is the default condition if this is the first time
            #coming across that character

            countT[t[i]] = 1 + countT.get(t[i], 0)

        if countS == countT:
            return True 
        else:
            return False
