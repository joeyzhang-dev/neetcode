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
**Space Complexity:** `O(n)`  
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

> 🧠 Elegant and efficient. Avoids division and handles edge cases like zeros gracefully. This is the ideal approach for interviews.

```
