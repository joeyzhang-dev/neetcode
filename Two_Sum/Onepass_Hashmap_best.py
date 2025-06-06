# OnePass Hashmap Solution (Best Solution)
# The matching pair with a number x = x - target
# To solve this in one pass, we will keep track of numbers we've already seen in a hashmap
# Each new number, we check if the complement exists in our hashmap
    # if we do: solution found!
    # if not: we store the number and its index in the map and move on


# map the numbers to indices, becuase we care about quickly checking if a specific value has been seen
# dict lookups by keys are O(1) on average
    # if we didn't do this it would be O(n) because now we are checking all the indexes for its value, defeating the purpose of hashmap

# Time O(n)
# Mem O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        historyMap = {} # val : index

        for i, n in enumerate(nums):
            complement = target - n
            if complement in historyMap:
                return [historyMap[complement], i]
            historyMap[n] = i
        return