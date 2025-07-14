# 347. Top K Frequent Elements

## 📚 Table of Contents

- [🧠 Summary](#-summary)
- [📄 Problem Statement](#-problem-statement)
- [🔎 Approach 1: Hash Map + Sort](#-approach-1-hash-map--sort)
- [⚙️ Approach 2: Hash Map + Min Heap](#-approach-2-hash-map--min-heap)
- [📘 DSA Concepts Explained](#-dsa-concepts-explained)
- [🧪 Test Cases](#-test-cases)
- [🧱 Interview Walkthrough (CLEAN)](#-interview-walkthrough-clean)
- [❌ Common Pitfalls](#-common-pitfalls)
- [📘 Glossary](#-glossary)

---

## 🧠 Summary

- Return the `k` most frequent elements in an integer list.
- ✅ Use a frequency map (hashmap) to count occurrences.
- ✅ Two good approaches:
  - **Sort all frequencies**, then grab top-k → clean but O(n log n)
  - **Min heap of size `k`** → avoids sorting everything, better for large `n`

**Best Solution:** Hash Map + Min Heap  
Efficient when `k` is small and input size is large.

---

## 📄 Problem Statement

[🔗 LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)  
> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. Return the answer in **any order**.

**Constraints:**
- 1 <= nums.length <= 10⁵
- 1 <= k <= number of unique elements

---

## 🔎 Approach 1: Hash Map + Sort

### 🧠 Idea (What’s Going On)

- First, **count how often each number appears** using a dictionary (hashmap)
- Store the results as `[frequency, number]` pairs in a list
- **Sort the list** by frequency (ascending), then pop off the last `k` elements

This is easy to understand and works fine if `n` isn’t too large.

---

**Time Complexity:** `O(n log n)` — due to sorting  
**Space Complexity:** `O(n)` — to store the frequency map and array

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # If num not in count, start at 0 → then add 1

        # Step 2: Create list of [frequency, number] pairs
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])

        # Step 3: Sort by frequency ascending
        arr.sort()

        # Step 4: Pop k most frequent
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # grab the number, not the frequency
        return res
```

> 🧠 Tip: `[freq, num]` ensures sort is based on frequency first.

---

## ⚙️ Approach 2: Hash Map + Min Heap

### 🧠 Idea (What’s Going On)

- Again, use a dictionary to **count frequencies**
- Then use a **min heap of size `k`** to track only the most frequent elements:
  - Push `(frequency, number)` into the heap
  - If the heap grows beyond size `k`, pop the least frequent
- At the end, you’re left with the top `k`

This avoids sorting the entire list — great for large datasets.

---

**Time Complexity:** `O(k log n)`  
**Space Complexity:** `O(n)`

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Push (freq, num) to heap
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)  # remove smallest freq

        # Step 3: Extract results
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])  # just the number
        return res
```

---

## 📘 DSA Concepts Explained

<details>
<summary>🔹 Hash Map (Dictionary)</summary>

A data structure that stores key-value pairs. Example: `{num: frequency}`.

```python
count[num] = 1 + count.get(num, 0)
```
This line increments the frequency if it exists, otherwise sets it to 1.
</details>

<details>
<summary>🔹 Min Heap (heapq)</summary>

A binary heap where the smallest value stays at the top.

In this problem, we push `(frequency, number)` pairs into the heap:

```python
heapq.heappush(heap, (freq, num))
heapq.heappop(heap)
```

📊 **Heap Growth Example:**  
For input `nums = [1,1,1,2,2,3]`, `k = 2`

Step-by-step heap state:

```text
Push (3, 1):         [(3, 1)]
Push (2, 2):         [(2, 2), (3, 1)]
Push (1, 3):         [(1, 3), (3, 1), (2, 2)]
→ size > 2 → pop (1, 3)

Final heap:          [(2, 2), (3, 1)]
```

🧠 This keeps only the top `k` frequent elements.

</details>

<details>
<summary>🔹 Tuple vs List</summary>

- Tuples use parentheses: `(a, b)`  
- Lists use brackets: `[a, b]`  
Tuples are used in heaps because they’re immutable and sort element-wise.
</details>

---

## 🧪 Test Cases

```python
assert set(Solution().topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
assert Solution().topKFrequent([1], 1) == [1]
assert set(Solution().topKFrequent([4,4,4,4,5,5,5,6,6], 2)) == set([4,5])
```

---

## 🧱 Interview Walkthrough (CLEAN)

### 🔍 1. Clarify
- ✅ k is valid and ≤ number of unique elements
- ✅ Return order doesn’t matter
- ✅ nums may contain duplicates

### 🔬 2. Examples
```python
nums = [1,1,1,2,2,3], k = 2 → [1,2]
nums = [1], k = 1 → [1]
nums = [1,2,3,4], k = 2 → any 2 values
```

### 💡 3. Brainstorm
- Brute force: sort + count — ❌ inefficient
- Hashmap + sort — ✅ simple and works
- Hashmap + heap — ✅ optimal if `k << n`

### 🧱 4. Plan
1. Count frequencies using a dict
2. Push `(frequency, number)` into a min heap
3. If heap > k, pop the smallest
4. Extract numbers from heap

### 🧠 5. Complexity
- Time: `O(n log k)`
- Space: `O(n)`

### ✅ 6. Wrap-Up
Used heap to avoid full sort and extract the top `k` most frequent efficiently.

---

## ❌ Common Pitfalls

- Confusing tuple `(1, 3)` with list `[1, 3]`
- Not understanding that `heapq` is a min heap by default
- Forgetting to pop when heap size > k
- Sorting all elements instead of tracking only `k`

---

## 📘 Glossary

| Term               | Meaning |
|--------------------|---------|
| Hash Map / Dict     | Stores key-value pairs, like `{3: 2}` for num → freq |
| Min Heap            | Priority queue where smallest value stays on top |
| Tuple `(a, b)`      | Immutable pair of values, used in heap comparison |
| Frequency Map       | Another term for `count` dictionary |
| `get(key, default)` | Returns the value for `key`, or `default` if missing |
