## Summary
- Check if lengths match first (early exit — anagrams must be same length)
- Use a **hashmap** to count character frequencies
- Alternative: sorting approach (simpler but less efficient)

**Best Solution: Hashmap with array**  
- Count characters in first string, decrement for second string, check if all counts are zero

## [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
**Precondition:** Strings contain only lowercase letters, anagrams must be same length

> 💡 Check if two strings contain the same characters with the same frequencies

---

### Approach 1: Hashmap with Array (Optimal)
**Time Complexity:** `O(n + m)`  
**Space Complexity:** `O(1)` (fixed 26-character array)  
**Idea:** Use a fixed-size array to count character frequencies. Increment for first string, decrement for second string, then check if all counts are zero.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            return False
    return True
```

> 🧠 Most efficient approach for lowercase letters. Uses a fixed-size array instead of a hashmap, making it O(1) space complexity.

---

### Approach 2: Two Hashmaps
**Time Complexity:** `O(n + m)`  
**Space Complexity:** `O(1)` (at most 26 different characters)  
**Idea:** Build separate hashmaps for each string, then compare character frequencies.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
```

> 🧠 More general approach that works with any character set. Uses `.get()` with default value to handle missing keys.

---

### Approach 3: Sorting
**Time Complexity:** `O(n log n + m log m)`  
**Space Complexity:** `O(1)` or `O(n + m)` (depending on sorting algorithm)  
**Idea:** Sort both strings and compare them directly.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)
```

> 🧠 Simplest approach but less efficient due to sorting. Letters have underlying ASCII values, so sorting puts them in the same order.

---

### Test Cases
```python
# Example test cases
assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False
assert isAnagram("", "") == True
```

---

### Notes
- Always check length equality first for early exit
- Array approach is optimal for lowercase letters only
- Hashmap approach is more general and works with any character set
- Sorting approach is simplest but least efficient
- All approaches handle edge cases like empty strings correctly 