class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                # we have to reutnr a list of the indices of both the numbers

                return [hashmap[number],index]
            
            #if the elemnt is not present in the hashmap
            # add it to the hashmap
            # this number in the hashmap has the index of : 
            hashmap[number] = index
