## Summary
- Return an array where each element is the product of all elements in the input array except itself.
- Division is **not allowed**, and the goal is to solve in `O(n)` time and `O(1)` space (excluding the output).
- Brute force works but is inefficient. Prefix and Postfix products yield a clean, optimal solution.

**Best Solution:** Prefix + Postfix Product  
- Build output by first storing prefix products, then multiplying by postfix products in a second pass.

---

## [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
**Precondition:**  
- `2 <= len(nums) <= 10^5`  
- `-30 <= nums[i] <= 30`  
- Product of all elements fits in a 32-bit integer  
- Division is not allowed

> 💡 For each index, compute product of all elements except the one at that index, without using division.

---

### Approach 1: Brute Force
**Time Complexity:** `O(n^2)`  
**Space Complexity:** `O(1) and O(n) if counting answer array`  
**Idea:**  
For each element, iterate through the array and multiply every value except the one at the current index.

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            product = 1
            for j in range(n):
                if j == i:
                    continue
                product *= nums[j]
            answer[i] = product
        return answer
```

> 🧠 Useful for understanding the problem but too slow for large inputs. Sets the stage for thinking about prefix/suffix strategies.

---

### Approach 2: Prefix and Postfix (Optimized)
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)` (output array not counted)  
**Idea:**  
Use two passes:  
- 1st pass: store prefix product at each index  
- 2nd pass: multiply current value by postfix product

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Example: nums = [1, 2, 3, 4]
        # Prefix pass:
        # answer = [1, 1, 2, 6]
        # Postfix pass:
        # answer = [24, 12, 8, 6]

        answer = [1] * len(nums)

        # Build prefix products
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Multiply by postfix products
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
```

---

### Test Cases
```python
s = Solution()

# ✅ Basic input
print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]

# ✅ Includes zero
print(s.productExceptSelf([1, 2, 0, 4]))  # [0, 0, 8, 0]

# ✅ Two elements
print(s.productExceptSelf([5, 6]))  # [6, 5]

# ✅ All ones
print(s.productExceptSelf([1, 1, 1, 1]))  # [1, 1, 1, 1]

# ✅ Negative numbers
print(s.productExceptSelf([-1, 2, -3, 4]))  # [-24, 12, -8, 6]
```

---

### Notes
- Cannot use division → eliminates simple total product + division method.
- Must handle **zero(s)** in the array:
  - One zero → result is zero everywhere except index of zero.
  - Two or more zeros → entire output is zero.
- Handles negative numbers and mixed signs properly.
- Prefix/Postfix avoids division and works in-place (space-efficient).

---

## 🗣️ Interview-Style Walkthrough (CLEAN Format)

### 🔍 1. Clarify and Understand the Problem
> “Rephrase the prompt clearly, confirm assumptions, and ask clarifying questions.”

**✅ Clarified Assumptions:**
- Input is a list of integers.
- At least two elements.
- Cannot use division.
- Output should not include the current index's value in the product.

---

### 🔬 2. Examples & Edge Cases

**Given Example:**  
Input: `[1,2,3,4]` → Output: `[24,12,8,6]`  
Explanation: Each number is the product of all other numbers.

**Custom Edge Cases:**  
- `[1, 2, 0, 4]` → `[0, 0, 8, 0]`  
- `[5, 6]` → `[6, 5]`  
- `[-1, 2, -3, 4]` → `[-24, 12, -8, 6]`  
- `[0, 0]` → `[0, 0]` (two zeros → all zero)

---

### 💡 3. Brainstorm Solutions

**Brute Force:**
> Try multiplying all elements for every index except the current one.

- Time: `O(n^2)`
- Space: `O(n)`
- ✅ Good for verifying logic
- ❌ Not scalable for large `n`

**Optimized Approach:**
> Use a prefix and postfix product pass to build answer in `O(n)` time.

- Time: `O(n)`
- Space: `O(1)` (excluding output)
- ✅ Clean and efficient
- ✅ Handles edge cases naturally

---

### 🧱 4. Implementation Plan (Talk Through Before Typing)

1. Create an output array initialized with 1s.
2. First pass: compute prefix product (left to right).
3. Second pass: multiply with postfix product (right to left).
4. Return the modified output array.

---

### 🧠 5. Code Complexity Analysis

- **Time Complexity:** `O(n)` — two linear passes over the input.
- **Space Complexity:** `O(1)` extra space — excluding output array.

---

### 🔍 6. Final Review & Wrap-Up

> “Code passes sample and custom test cases. Used prefix and postfix passes to avoid division. Time and space are optimal. Ready for follow-ups if any.”

✅ Clean solution  
✅ Edge cases handled  
✅ No division used  
✅ Efficient time/space  


> 🧠 Elegant and efficient. Avoids division and handles edge cases like zeros gracefully. This is the ideal approach for interviews.

```

---

## 📊 Visual Intuition: Prefix + Postfix Diagram

Let’s walk through the optimized approach on the input:

```python
nums = [1, 2, 3, 4]
```

### 🔁 Step 1: Prefix Pass (Left to Right)

We’ll build an intermediate result by storing the **product of all elements before each index**.

Initialize:

```
answer = [1, 1, 1, 1]
prefix = 1
```

Iterate:

| i | nums[i] | answer[i] = prefix | update prefix → prefix *= nums[i] |
|---|---------|--------------------|----------------------------------|
| 0 |    1    |         1          |         prefix = 1 × 1 = 1       |
| 1 |    2    |         1          |         prefix = 1 × 2 = 2       |
| 2 |    3    |         2          |         prefix = 2 × 3 = 6       |
| 3 |    4    |         6          |         prefix = 6 × 4 = 24      |

🔎 After prefix pass:

```python
answer = [1, 1, 2, 6]
```

Each index holds the **product of all elements to its left**.

---

### 🔁 Step 2: Postfix Pass (Right to Left)

Now we multiply by the **product of all elements after each index**.

Initialize:

```
postfix = 1
```

Iterate in reverse:

| i | nums[i] | answer[i] *= postfix | update postfix → postfix *= nums[i] |
|---|---------|----------------------|------------------------------------|
| 3 |    4    |      6 × 1 = 6       |        postfix = 1 × 4 = 4         |
| 2 |    3    |      2 × 4 = 8       |        postfix = 4 × 3 = 12        |
| 1 |    2    |      1 × 12 = 12     |        postfix = 12 × 2 = 24       |
| 0 |    1    |      1 × 24 = 24     |        postfix = 24 × 1 = 24       |

🔎 Final output:

```python
answer = [24, 12, 8, 6]
```

---

## 🧠 Why This Works

- For index `i`, we split the product into:
  - All elements **before** → prefix
  - All elements **after** → postfix
- By doing 2 passes, we compute both without ever including `nums[i]` in the multiplication.
- This avoids division, handles zeros safely, and runs in linear time.

✅ Clean  
✅ Constant extra space  
✅ No edge case hacks

---

## 🔁 Visualization Recap

```
nums   = [1, 2, 3, 4]
prefix = [1, 1, 2, 6]      ← left products (excluding current)
postfx = [24,12, 4, 1]     ← right products (excluding current)
result = [24,12, 8, 6]     ← element-wise: prefix[i] * postfix[i]
```

This approach builds intuition for **building up** and then **folding down** through the array — a powerful pattern for many array problems.

