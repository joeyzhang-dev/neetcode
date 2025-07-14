## Summary

- Problem: Return the `k` most frequent elements in a list of integers.
- Naive idea: Sort the array and count streaks manually — not efficient.
- Optimal idea: Use a hash map to count frequencies, then either:
  - Sort the entries by frequency (O(n log n))
  - Use a heap to keep only top k (O(n log k))

**Best Solution:** Hash Map + Min Heap

- Count frequencies using a dictionary, then push (frequency, number) pairs into a min-heap of size `k`. The heap always keeps the top `k` most frequent elements, and we return them at the end.

## [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

**Precondition:** 1 <= nums.length <= 10^5, k is always valid (1 <= k <= number of unique elements)

> 💡 Return the `k` most frequent elements from the list `nums`. Order does not matter.

---

### Approach 1: Hash Map + Sort

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(n)`

**Idea:**
1. Count frequencies using a dictionary `count[num] = frequency`
2. Convert count map to a list of `[freq, num]`
3. Sort the list by frequency
4. Pop the top `k` from the end

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()  # ascending by freq

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
```

---

### Approach 2: Hash Map + Min Heap (Optimal for large `n`, small `k`)

**Time Complexity:** `O(n log k)`  
**Space Complexity:** `O(n)`

**Idea:**
1. Build a **frequency map** using a dictionary
2. Use a **min heap** (priority queue) to maintain top `k` most frequent elements
3. Heap stores **tuples** `(freq, num)` so the least frequent is always on top
4. Pop all elements from the heap to get the top `k`

```python
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # Dictionary: key → num, value → frequency

        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))  # push tuple
            if len(heap) > k:
                heapq.heappop(heap)  # remove least frequent

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
```

---

### 🔍 DSA Concepts Explained

**🧩 Dictionary / Hash Map**  
Maps keys to values efficiently.  
Example:  
```python
count = {}
count[3] = 1
```
means `count` maps `3 → 1`.

**🧩 `count.get(num, 0)`**  
Returns the count of `num` if it exists; returns 0 if not.  
Used to avoid `KeyError`.

**🧩 Tuple `(freq, num)`**  
A **tuple** is a fixed-size grouping in Python using parentheses.  
This tuple is used in the heap so we can compare by frequency (`heapq` compares first item in tuple).

**🧩 Min Heap (`heapq`)**  
Python’s built-in heap implementation is a **min-heap**.  
By default, `heapq.heappop()` removes the **smallest** element.  
We use this to evict the lowest frequency when the heap size exceeds `k`.

---

### Test Cases

```python
assert set(Solution().topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
assert Solution().topKFrequent([1], 1) == [1]
assert set(Solution().topKFrequent([4,4,4,4,5,5,5,6,6], 2)) == set([4,5])
```

---

### Interview-Style Walkthrough (CLEAN Format)

#### 🔍 1. Clarify the Problem
> “Return the `k` most frequent elements from an integer list. Order doesn’t matter.”

- ✅ `k` is valid
- ✅ Duplicates allowed
- ✅ Return any order

---

#### 🔬 2. Examples & Edge Cases

```python
[1,1,1,2,2,3], k = 2 → [1,2] or [2,1]
[1], k = 1 → [1]
[1,2,3,4], k = 2 → any 2 values
```

---

#### 💡 3. Brainstorm

- Brute: sort and count manually (O(n log n))
- Sort: use hashmap + list + sort (O(n log n))
- Heap: hashmap + min-heap of size k (O(n log k)) ✅ best for large inputs

---

#### 🧱 4. Plan

1. Use a dict to count `num → frequency`
2. Push `(freq, num)` into heap
3. Keep size ≤ `k` by popping smallest
4. Extract final result from heap

---

#### 🧠 5. Complexity

- **Time:** O(n log k)
- **Space:** O(n)

---

#### ✅ 6. Wrap-Up

This problem reinforces:
- Tuple usage in Python
- Frequency counting with `get`
- Heap-based prioritization for top-k problems

Prefer this approach when `n` is large and `k` is small.

---
