class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0, len(numbers) -1

        while l<r and l != r:
            if numbers[l] + numbers[r] < target:
                l = l+1
            elif numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                return [l+1,r+1]
