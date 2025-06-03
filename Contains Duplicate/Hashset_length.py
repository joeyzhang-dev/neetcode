# We can use a hashset to keep a counter for each character
# if there are no duplicates then there is no more than 1 of each character
# If there are duplicates then the hashset will have a smaller length than the array's

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)