## Summary
- Use a **hashset** to track previously seen values for optimal performance
- Alternative approaches: sorting (space-efficient) or brute force (simple but slow)
- Early exit when duplicate is found

**Best Solution: Hashset approach**  
- Track seen values in a set, return True if current value already exists

## [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
**Precondition:** Array of integers, can contain negative numbers

> 💡 Check if any value appears at least twice in the array

---

### Approach 1: Hashset (Optimal)
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
**Idea:** Use a hashset to keep track of previously seen values. If we encounter a value that's already in the set, we've found a duplicate.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```

> 🧠 This is the most efficient approach. We trade space for time by using a hashset for O(1) lookups. Early exit when duplicate is found.

---

### Approach 2: Hashset Length Comparison
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
**Idea:** Convert array to set and compare lengths. If there are duplicates, the set will be smaller than the original array.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

> 🧠 Very concise one-liner solution. Same time/space complexity as Approach 1, but doesn't allow early exit.

---

### Approach 3: Sorting
**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(1)` (not counting sorting space)  
**Idea:** Sort the array first. Duplicates will be adjacent to each other, so we can check consecutive elements.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

> 🧠 Space-efficient approach that doesn't require extra data structure. However, sorting modifies the original array and has worse time complexity.

---

### Approach 4: Brute Force
**Time Complexity:** `O(n²)`  
**Space Complexity:** `O(1)`  
**Idea:** Check every possible pair of elements to find duplicates.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
```

> 🧠 Simple to understand but very inefficient. Only use for educational purposes or when space is extremely limited.

---

### Test Cases
```python
# Example test cases
assert hasDuplicate([1,2,3,1]) == True
assert hasDuplicate([1,2,3,4]) == False
assert hasDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
```

---

### Notes
- Hashset approach is optimal for most cases
- Consider sorting approach if space is limited and array can be modified
- Brute force is only useful for learning or very small arrays
- All approaches handle edge cases like empty arrays or single elements correctly 