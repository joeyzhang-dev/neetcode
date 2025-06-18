# check every possible combination of two numbers one by one until 
# we find a solution

# Time: O(n^2) -> nested loops
# Space O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
