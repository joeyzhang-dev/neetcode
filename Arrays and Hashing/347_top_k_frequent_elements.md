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
- ✅ Use either:
  - Sort by frequency (O(n log n))
  - Min heap of size `k` (O(n log k)) ← optimal for large input

**Best Solution:** Hash Map + Min Heap  
Efficiently tracks top-k elements without sorting all frequencies.

---

## 📄 Problem Statement

[🔗 LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)  
> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. Return the answer in **any order**.

**Constraints:**
- 1 <= nums.length <= 10⁵
- 1 <= k <= number of unique elements

---

## 🔎 Approach 1: Hash Map + Sort

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()  # sort by frequency ascending

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])  # pop most frequent
        return res
```

> ✅ Sort by frequency and pop last `k` elements.

---

## ⚙️ Approach 2: Hash Map + Min Heap

**Time Complexity:** `O(n log k)`  
**Space Complexity:** `O(n)`

```python
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))  # (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
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
Push (2, 2):         [(2, 2), (3, 1)]      ← valid (size ≤ k)
Push (1, 3):         [(1, 3), (3, 1), (2, 2)]
   → size > 2 → pop (1, 3)

Final heap:          [(2, 2), (3, 1)]
```

🧠 This keeps only the top `k` frequent elements by evicting the least frequent when the heap exceeds size `k`.

</details>

<details>
<summary>🔹 Tuple vs List</summary>

- Tuples use parentheses: `(a, b)`  
- Lists use brackets: `[a, b]`  
Tuples are often used in heaps because they are immutable and support element-wise comparison.

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
- ✅ `k` is valid
- ✅ Return order doesn't matter
- ✅ nums may have duplicates

### 🔬 2. Examples
```python
nums = [1,1,1,2,2,3], k = 2 → [1,2]
nums = [1], k = 1 → [1]
nums = [1,2,3,4], k = 2 → any 2 values
```

### 💡 3. Brainstorm
- Brute force: sort and count manually — ❌ too slow
- Hashmap + sort by freq — ✅ clean
- Hashmap + heap — ✅ optimal if `k << n`

### 🧱 4. Implementation Plan
1. Build a frequency map using `count[num] = 1 + count.get(num, 0)`
2. Push each `(freq, num)` into a min heap
3. Keep size ≤ `k` by popping smallest
4. Extract elements from heap

### 🧠 5. Complexity
- Time: `O(n log k)`
- Space: `O(n)`

### ✅ 6. Wrap-Up
Used frequency counting and a heap to keep the top `k` frequent elements. Avoided full sorting for better performance.

---

## ❌ Common Pitfalls

- Confusing tuple `(1, 3)` with list `[1, 3]`
- Forgetting `heapq` is a **min heap** by default
- Not popping when heap size > k
- Sorting the whole list when only top `k` needed

---

## 📘 Glossary

| Term               | Meaning |
|--------------------|---------|
| Hash Map / Dict     | Stores key-value pairs, like `{3: 2}` for num → freq |
| Min Heap            | Priority queue where smallest value stays on top |
| Tuple `(a, b)`      | Immutable pair of values, used in heap comparison |
| Frequency Map       | Another term for `count` dictionary |
| `get(key, default)` | Returns the value for `key`, or `default` if missing |
