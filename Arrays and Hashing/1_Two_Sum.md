## Summary
- Use a **hashmap** to store previously seen values and their indices
- Key insight: for each number, check if its complement (target - current) exists in the hashmap
- Early exit when complement is found

**Best Solution: One-pass hashmap**  
- Store each number and its index as we iterate, check for complement

## [1. Two Sum](https://leetcode.com/problems/two-sum/)
**Precondition:** Array of integers, exactly one solution exists, cannot use the same element twice

> 💡 Find two numbers in the array that add up to the target value and return their indices

---

### Approach 1: One-pass Hashmap (Optimal)
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
**Idea:** Use a hashmap to store each number and its index as we iterate. For each new number, check if its complement (target - current) already exists in the hashmap.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        historyMap = {} # val : index

        for i, n in enumerate(nums):
            complement = target - n
            if complement in historyMap:
                return [historyMap[complement], i]
            historyMap[n] = i
        return []
```

> 🧠 This is the most efficient approach. We trade space for time by using a hashmap for O(1) lookups. The key insight is that we store each number as we see it, then check if its complement exists.

**Key Points:**
- `historyMap = {}` stores value → index mapping
- `complement = target - n` calculates what we need to find
- `if complement in historyMap` checks if we've seen the complement before
- `historyMap[n] = i` stores current number and its index for future lookups

---

### Approach 2: Brute Force
**Time Complexity:** `O(n²)`  
**Space Complexity:** `O(1)`  
**Idea:** Check every possible combination of two numbers using nested loops until we find a pair that sums to the target.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

> 🧠 Simple to understand but very inefficient. Only use for educational purposes or when space is extremely limited.

---

### Test Cases
```python
# Example test cases
assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
```

---

### Notes
- Hashmap approach is optimal for most cases
- Brute force is only useful for learning or very small arrays
- The hashmap approach works because we're guaranteed exactly one solution
- Both approaches handle edge cases correctly
- Remember that we cannot use the same element twice, but the hashmap approach naturally handles this 