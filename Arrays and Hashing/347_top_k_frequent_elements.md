## Summary

- Problem: Return the `k` most frequent elements in a list of integers.
- Naive idea: Sort the array and count streaks manually — not efficient.
- Optimal idea: Use a hash map to count frequencies, then sort by frequency.

**Best Solution:** Hash Map + Frequency Sort

- Count frequencies using a dictionary, then sort and return the top `k` most frequent elements. This is simple, modular, and scales well.

## [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

**Precondition:** 1 <= nums.length <= 10^5, k is always valid (1 <= k <= number of unique elements)

> 💡 Return the `k` most frequent elements from the list `nums`. Order does not matter.

---

### Approach 1: Hash Map + Sort

**Time Complexity:** `O(n log n)` – sorting the array of unique elements based on frequency.\
**Space Complexity:** `O(n)` – for frequency map and temporary arrays.

**Idea:**

1. Count frequencies using a dictionary `count[num] = frequency`
2. Turn `count.items()` into a list of `[freq, num]` pairs
3. Sort the list in ascending frequency
4. Pop the last `k` elements (highest frequencies)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # if new key, add with value 1
            # if existing, increment

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()  # sort by freq ascending

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # pop most frequent

        return res
```

> 🧠 We use `[freq, num]` to sort by frequency first, then extract the number.

---

### 🔍 Step-by-Step Visualization

Example: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`

**1. Build frequency map:**

```python
count = {
    1: 3,
    2: 2,
    3: 1
}
```

**2. Convert to sortable array:**

```python
arr = [
    [3, 1],
    [2, 2],
    [1, 3]
]
```

**3. Sort ascending by frequency:**

```python
arr = [
    [1, 3],
    [2, 2],
    [3, 1]
]
```

**4. Pop last **``** entries:**

```python
res = []
# First pop → [3, 1] → res = [1]
# Second pop → [2, 2] → res = [1, 2]
```

✅ Final result: `[1, 2]`

---

### Test Cases

```python
assert Solution().topKFrequent([1,1,1,2,2,3], 2) in [[1,2], [2,1]]
assert Solution().topKFrequent([1], 1) == [1]
assert Solution().topKFrequent([4,4,4,4,5,5,5,6,6], 2) in [[4,5], [5,4]]
```

---

### Notes

- Avoid the naive idea of sorting and manually counting streaks — it's verbose and error-prone.
- Using `count[num] = 1 + count.get(num, 0)` avoids needing conditionals to initialize.
- Sorting `[freq, num]` makes it easy to grab top-k using `.pop()`.

---

## 🔍 Interview-Style Walkthrough (CLEAN Format)

### 🔍 1. Clarify and Understand the Problem

> "Given a list of integers, return the top `k` most frequent elements. Order doesn’t matter."

**✅ Clarified Assumptions:**

- k is always <= number of unique elements
- nums may have duplicates
- Return order doesn't matter

---

### 🔬 2. Examples & Edge Cases

**Given Example:**\
`nums = [1,1,1,2,2,3], k = 2` → `[1,2]` or `[2,1]`

**Custom Edge Cases:**

- All elements same → `[1,1,1,1], k = 1` → `[1]`
- Each element unique → `[1,2,3,4], k = 2` → any two numbers

---

### 💡 3. Brainstorm Solutions

**Brute Force:**

- Sort nums, walk through and manually count streaks
- Compare streaks to maintain top-k
- ❌ Too verbose, requires full sort `O(n log n)` and edge-case juggling

**Optimized Approach:**

- Count with hashmap `O(n)`
- Sort by frequency `O(m log m)` where m = number of unique elements
- Extract top-k via pop
- ✅ Much cleaner and easier to reason about

---

### 🧱 4. Implementation Plan (Talk Through Before Typing)

1. Count each number’s frequency using a dict
2. Build a list of [freq, num] for sorting
3. Sort ascending
4. Pop last k elements’ num values

---

### 🧠 5. Code Complexity Analysis

- **Time:** `O(n + m log m)`
  - `n` for frequency counting
  - `m log m` to sort unique elements
- **Space:** `O(n)` for dict + result

---

### 🔍 6. Final Review & Wrap-Up

> “This solution uses a frequency map to count occurrences in linear time, then sorts the frequency list and pops the top-k most frequent elements. It avoids the fragility of manual streak logic and performs well for typical constraints.”

