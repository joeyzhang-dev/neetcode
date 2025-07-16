
## Summary
- Return an array where each element is the product of all elements in the input array except itself.
- Division is **not allowed**, and a brute force approach leads to `O(n^2)` time complexity.
- This initial solution is meant to verify correctness and explore problem structure.

**Best Solution:** Brute Force (Initial Pass)  
- Iterate through all elements, skipping the current index, and compute the product manually.

---

## [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
**Precondition:**  
- `2 <= len(nums) <= 10^5`  
- `-30 <= nums[i] <= 30`  
- Product of all elements fits in a 32-bit integer  
- Division is not allowed

> 💡 Compute the product of all array elements except for the current one.

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
        # Given:
            # nums : arr[int] - at least 2 elements
        # Return:
            # answer : arr[int] - answer[i] = product of all elements except nums[i]

        # Brute force: 
            # Time O(n^2) | Space O(n)
            # We evaluate each index i and skip it while computing the product

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
```
