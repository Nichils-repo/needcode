#using sets

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
    
            hashset.add(n)
        
        return False


# using hashmaps 

class Solutions : 
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num,0) + 1
        return False
    

#using length of hashset 

class Solution :
    def hasDuplicate(self, nums: List[int])-> bool:
        
        new_num = set(nums)

        if(len(new_num) == len(nums)):
            return True
        else:
            return False



    
# sorting solution :

class Solution :
    def hasDuplicate(self, nums: List[int])-> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i+1]:
                return True
            else :
                return False
            
