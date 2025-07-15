# 347. Top K Frequent Elements

## 📚 Table of Contents

- [🧠 Summary](#-summary)
- [📄 Problem Statement](#-problem-statement)
- [🔎 Approach 1: Hash Map + Sort](#-approach-1-hash-map--sort)
- [⚙️ Approach 2: Hash Map + Min Heap](#-approach-2-hash-map--min-heap)
- [🔢 Approach 3: Bucket Sort](#-approach-3-bucket-sort)
- [📜 DSA Concepts Explained](#-dsa-concepts-explained)
- [🧪 Test Cases](#-test-cases)
- [🧱 Interview Walkthrough (CLEAN)](#-interview-walkthrough-clean)
- [❌ Common Pitfalls](#-common-pitfalls)
- [📜 Glossary](#-glossary)

---

## 🧠 Summary

- Return the `k` most frequent elements in an integer list.
- ✅ Use a frequency map (hashmap) to count occurrences.
- ✅ Three good approaches:
  - **Sort all frequencies**, then grab top-k → clean but O(n log n)
  - **Min heap of size **`` → avoids sorting everything, better for large `n`
  - **Bucket sort** → best time complexity (O(n)) if frequency bounds are known

**Best Solution:** Hash Map + Min Heap (most general-purpose)\
**Most Optimal Time:** Bucket Sort (O(n)), but more specialized

---

## 📄 Problem Statement

[🔗 LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. Return the answer in **any order**.

**Constraints:**

- 1 <= nums.length <= 10⁵
- 1 <= k <= number of unique elements

---

## 🔎 Approach 1: Hash Map + Sort

**Time Complexity:** `O(n log n)` — due to sorting\
**Space Complexity:** `O(n)` — to store the frequency map and array

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Create list of [frequency, number] pairs
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])

        # Step 3: Sort by frequency ascending
        arr.sort()

        # Step 4: Pop k most frequent
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```

> 🧠 Tip: `[freq, num]` ensures sort is based on frequency first.

---

## ⚙️ Approach 2: Hash Map + Min Heap

**Time Complexity:** `O(n log k)`\
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

## 🔢 Approach 3: Bucket Sort

**Time Complexity:** `O(n)`

- Counting frequencies = O(n)
- Building buckets = O(n)
- Scanning buckets from high to low = O(n)

**Space Complexity:** `O(n)`

- Hashmap = O(n)
- Buckets = O(n)
- Output = O(k) ≤ O(n)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Bucket elements by frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Gather top k from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
```

### 🔬 Visualization

**Input:** `nums = [1,1,1,2,2,3]`, `k = 2`

**Frequency Map:**

```python
{
  1: 3,
  2: 2,
  3: 1
}
```

**Buckets (index = frequency):**

```python
[
  [],        # freq 0 (unused)
  [3],       # freq 1
  [2],       # freq 2
  [1]        # freq 3
]
```

Start from end and collect top k → `[1, 2]`

---

## 📜 DSA Concepts Explained

Stores key-value pairs like `{element: frequency}`. Useful for counting occurrences efficiently in O(1) average time per insert.

A priority queue where the smallest element is always at the top. Used here to keep track of the top `k` frequent elements efficiently.

Instead of sorting or maintaining a heap, we use a list of lists (buckets) where the index represents frequency. It's efficient when frequencies are bounded.

---

## 🧪 Test Cases

```python
assert set(Solution().topKFrequent([1,1,1,2,2,3], 2)) == {1, 2}
assert Solution().topKFrequent([1], 1) == [1]
assert set(Solution().topKFrequent([4,4,4,5,5,6], 2)) == {4, 5}
assert set(Solution().topKFrequent([5,7,5,7,5,7,8], 2)) == {5, 7}
```

---

## 🧱 Interview Walkthrough (CLEAN)

### 🔍 1. Clarify and Understand the Problem

- ✅ Input is a list of integers
- ✅ `k` is guaranteed to be valid (≤ number of unique elements)
- ✅ Return order does not matter

### 🔬 2. Examples & Edge Cases

```python
Input: [1,1,1,2,2,3], k = 2 → Output: [1,2] or [2,1]
Input: [1], k = 1 → Output: [1]
Input: [1,2,3,4,5], k = 3 → Output: any 3 distinct values
```

### 💡 3. Brainstorm Solutions

- Brute force: Count then sort → O(n log n)
- Min heap: Track top k in O(n log k)
- Bucket sort: Group by frequency index → O(n) if frequency range is bounded

### 🧱 4. Implementation Plan

1. Count frequencies using a dictionary
2. Apply sorting, heap, or bucket logic
3. Extract top k frequent elements

### 🧠 5. Code Complexity Analysis

- Sort: O(n log n)
- Heap: O(n log k)
- Bucket: O(n)
- Space: All are O(n) due to frequency map and output

### 🔍 6. Final Review & Wrap-Up

✅ Covered multiple solutions with tradeoffs\
✅ Handled edge cases and verified correctness

---

## ❌ Common Pitfalls

- ❗ Forgetting that `heapq` in Python is a min heap by default
- ❗ Confusing tuple vs list when pushing into the heap: `(freq, num)` not `[freq, num]`
- ❗ Not scanning the bucket array in reverse (from high frequency to low)
- ❗ Assuming the result has to be in a specific order (it doesn't)

---

## 📜 Glossary

| Term             | Definition                                                   |
| ---------------- | ------------------------------------------------------------ |
| Hash Map         | A key-value store for counting or lookups in O(1) avg time   |
| Min Heap         | A binary heap where the root is the smallest element         |
| Bucket Sort      | A sorting technique using a frequency-indexed array of lists |
| Time Complexity  | An estimate of algorithm speed using Big-O notation          |
| Space Complexity | An estimate of memory usage growth in terms of input size    |

