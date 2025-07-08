## Summary
- Classic hashmap lookup problem: find two indices such that their values add up to a target.
- Brute force checks all pairs (slow), but optimal is a one-pass hashmap for `O(n)` time.
- Key optimization: track each value’s index as you iterate, and check if the complement already exists.
- Guaranteed one solution, so we can return early on match.

**Best Solution:** One-Pass Hashmap  
- Efficient because we check and store values in a single pass, enabling `O(1)` lookups per element using a dictionary.

## [1. Two Sum](https://leetcode.com/problems/two-sum/)
**Precondition:** Array of integers `nums`, integer `target`, exactly one valid pair exists, cannot use same element twice

> 💡 Given a list of integers, return the *indices* of the two numbers that add up to a target.

---

### Approach 1: One-Pass Hashmap
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`  
**Idea:** As we iterate through the array, store each value and its index in a hashmap. For each new number, compute its complement (`target - number`) and check if that complement has already been seen.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in history:
                return [history[complement], i]
            history[n] = i
        return []
```

> 🧠 Hashmap gives constant-time lookups. Storing each element after checking avoids using the same element twice. Early exit on match.

---

### Approach 2: Brute Force
**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1)`  
**Idea:** Check every pair of indices `(i, j)` where `j > i`. If `nums[i] + nums[j] == target`, return `[i, j]`.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

> 🧠 Useful for learning or very small input, but becomes slow quickly due to double loop. No extra space needed.

---

### Test Cases
```python
assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
assert Solution().twoSum([3, 3], 6) == [0, 1]
```

---

### Notes
- Only one solution exists — safe to return on first match.
- Duplicate values are okay (e.g. `[3, 3]`) because dictionary handles mapping distinct indices.
- `enumerate(nums)` gives `(index, value)` cleanly.
- Hashmap stores `value → index`, not the other way around.

---

## 🗣️ Interview-Style Walkthrough (CLEAN Format)

### 🔍 1. Clarify and Understand the Problem
> “So I’m given a list of integers and a target sum. I need to return the indices of two numbers that add up to the target. Each input will have exactly one solution, and I can’t use the same element twice. Is that correct?”

**✅ Clarified Assumptions:**
- List is non-empty and has at least two elements
- There’s always one valid solution
- Values can be negative or zero
- Indices must be returned, not the values themselves

---

### 🔬 2. Examples & Edge Cases

**Given Example:**  
- `nums = [2, 7, 11, 15], target = 9` → `[0, 1]` because 2 + 7 = 9

**Custom Edge Cases:**  
- `nums = [3, 3], target = 6` → `[0, 1]` (duplicate values)
- `nums = [-1, -2, -3, -4, -5], target = -8` → `[2, 4]`
- `nums = [1, 2], target = 3` → `[0, 1]`

---

### 💡 3. Brainstorm Solutions

**Brute Force:**
> “Loop through all pairs `(i, j)` with `j > i`, check if `nums[i] + nums[j] == target`.”

- Time: `O(n^2)`
- Space: `O(1)`
- ✅ Works reliably, no extra structures
- ❌ Too slow for large inputs

**Optimized Approach: One-Pass Hashmap**
> “Iterate once, storing each number and index in a dictionary. For each value, compute complement = target - value. If complement is already in the dict, return the pair.”

- Time: `O(n)`
- Space: `O(n)`
✅ Fast, handles all cases efficiently  
🧠 Dictionary allows constant-time lookups

---

### 🧱 4. Implementation Plan (Talk Through Before Typing)

1. Create an empty dictionary `history`
2. Loop through `nums` with `enumerate` to get index + value
3. For each number:
   - Compute complement = `target - num`
   - If complement is in `history`, return `[history[complement], i]`
   - Else, store `num: i` in `history`
4. If no solution found (not expected due to prompt), return `[]`

---

### 🧠 5. Code Complexity Analysis

- **Time Complexity:** `O(n)` — iterate once
- **Space Complexity:** `O(n)` — in worst case, all elements stored

---

### 🔍 6. Final Review & Wrap-Up

> “This solution is clean, efficient, and leverages a hashmap for constant-time lookup. It handles negative numbers, duplicates, and returns early once a valid pair is found. We avoid re-using the same element because we store only after checking for the complement.”

✅ Passed given and custom tests  
✅ Discussed brute force vs optimal  
✅ Offered clarity in edge cases  
✅ Ready for follow-ups (e.g. return *all* pairs, or handle no solution)

---
