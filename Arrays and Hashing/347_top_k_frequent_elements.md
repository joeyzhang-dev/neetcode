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

## 📄 Problem Statement

[🔗 LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. Return the answer in **any order**.

**Constraints:**

- 1 <= nums.length <= 10⁵
- 1 <= k <= number of unique elements

---

## 📜 DSA Concepts Explained

A data structure that stores key-value pairs. Example: `{num: frequency}`.

```python
count[num] = 1 + count.get(num, 0)
```

This line increments the frequency if it exists, otherwise sets it to 1.

A binary heap where the smallest value stays at the top.

In this problem, we push `(frequency, number)` pairs into the heap:

```python
heapq.heappush(heap, (freq, num))
heapq.heappop(heap)
```

📊 **Heap Growth Example:**\
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

- Tuples use parentheses: `(a, b)`
- Lists use brackets: `[a, b]`\
  Tuples are used in heaps because they’re immutable and sort element-wise.

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
- Bucket sort — ✅ O(n) time, best if k is large or we need linear time

### 🧱 4. Plan

1. Count frequencies using a dict
2. (a) Sort + pop k (b) Heap with k-size (c) Bucket with freq index
3. Extract top k

### 🧠 5. Complexity

- Sort: O(n log n)
- Heap: O(n log k)
- Bucket: O(n)

### ✅ 6. Wrap-Up

Each solution has its tradeoffs. Bucket sort gives linear time, heap gives memory-efficient top-k selection.

---

## ❌ Common Pitfalls

- Confusing tuple `(1, 3)` with list `[1, 3]`
- Not understanding that `heapq` is a min heap by default
- Forgetting to pop when heap size > k
- Sorting all elements instead of tracking only `k`
- Misusing bucket indices or forgetting max freq = len(nums)

---

## 📜 Glossary

| Term                | Meaning                                              |
| ------------------- | ---------------------------------------------------- |
| Hash Map / Dict     | Stores key-value pairs, like `{3: 2}` for num → freq |
| Min Heap            | Priority queue where smallest value stays on top     |
| Tuple `(a, b)`      | Immutable pair of values, used in heap comparison    |
| Frequency Map       | Another term for `count` dictionary                  |
| `get(key, default)` | Returns the value for `key`, or `default` if missing |

