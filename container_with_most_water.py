class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # bruteforce approach 

        result = 0

        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                # area = lenght * breadth
                # length will be difference b/w both pointers
                area = (r-l) * (min(heights[r], heights[l]))
                # since the shorter height will be the 
                #maximum usable height in this scenario

                result = max(area, result)



        #optimized apporach -> two pointer 
        result = 0
        l,r = 0, len(heights) -1 

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            result = max(result,area)

            if heights[l] < heights[r]:
                l = l + 1 
            
            elif heights[r] < heights[l]:
                r = r -1 
            else: # if both are equal we can change l or r
                r = r -1
            # we can also combine the else and elif 
            # cuz they are doing the same thing 

        return result  

