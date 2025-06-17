class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i, number in enumerate(nums):
            if i > 0 and number == nums[i-1]:
                continue 
            l, r= i+1, len(nums) -1
            while r > l:
                threesum = number + nums[l] + nums[r]
                if threesum > 0:
                    r = r -1 
                elif threesum < 0:
                    l = l + 1
                else: #threesum == 0
                    result.append([number, nums[l], nums[r]])

                    #update pointer at the end to find the next threesum of the same i
                    l = l +1 
                    r= r-1 
                    while r>l and nums[l] == nums[l-1]:
                        l = l +1
                    while r> l and nums[r] == nums [r+1]:
                        r = r-1
                    # basically 
                    # if there is some solution, even l and r cant be the same the prev l,r
                    # if there is -3 3 0
                    # -3 _ 0 => has only one correct answer ie 3
                    # -3 3 _ => has only one correct answer ie 0
                    ### thus, after we found the first threesum = 0, which checking for more
                    #with the same i, we gotta avoid more l and r of the same value 
                    #also we dont have to update both for the next threesum, technically 
                    #only updating l or r is enough, as due to the prev loop, they will
                    #automatically be corrected 
                    # say -3 -3 -2 0 1 2 3
                    # if we found out -3 , 3, 0
                    # and next if we check if l is same as prev 
                    # if it is the same, then it will move the pointer to the next
                    #this will cause the threesum to change 
                    #thus it will automatically cuase the right pointer to change 
                    #so only one the conditions in the last is required, but its fine even 
                    #if we have both
                    
        return result
