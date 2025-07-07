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

> 💡 A `set()` is a built-in Python data structure that stores **unique values** and provides **O(1)** average-time lookup. It's backed by a **hash table**, and unlike a dictionary, it only tracks **keys**, not key-value pairs.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()  # Create an empty set to store unique elements

        for n in nums:
            if n in hashset:
                # If we've already seen this number, it's a duplicate
                return True
            # Otherwise, add the number to the set
            hashset.add(n)

        # If we finish the loop without finding duplicates, return False
        return False
```

> 🧠 This is the most efficient approach.  
> - We trade space for time by using a set for constant-time lookups  
> - No need to count elements or sort the array  
> - Sets only store **keys**, which is all we need in this case  
> - Ideal when you want to **track seen elements quickly**

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
Even though the inner loop shrinks as `i` increases, the total number of comparisons is:

$$
\sum_{i=0}^{n-1} (n - i - 1) = \frac{n(n-1)}{2}
$$

which is still \(O(n^2)\) in Big-O notation.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
```

> 🧠 Simple to understand but very inefficient. The total number of pairwise checks grows quadratically with input size. Only use for educational purposes or very small arrays.

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
