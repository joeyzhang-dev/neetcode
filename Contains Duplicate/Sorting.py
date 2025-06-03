#Duplicates will be right next to each other
# Check if the pointer is the same as the previous value

# Time: O(nlogn) 
# Space: O(1) not counting space used by sorting algorithm
 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False