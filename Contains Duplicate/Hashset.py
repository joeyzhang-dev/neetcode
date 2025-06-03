# 
# Use a hashset to keep a history of previously seen values
# If we've never seen a match then we add it to our hashset
# eventually we will find duplicates if thers is one

# Time: O(n) 
# Space: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
