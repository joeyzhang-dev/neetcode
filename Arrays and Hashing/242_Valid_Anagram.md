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


## 🗣️ Interview-Style Walkthrough (CLEAN Format)

### 🔍 1. Clarify and Understand the Problem
> "We’re given two strings, and we need to return `True` if they are anagrams — meaning they must contain the same characters in the same frequency. So order doesn’t matter, but letter counts do."
> 
> "Are we guaranteed the input will be lowercase English letters only? Any non-alphabetic characters or null cases I should be aware of?"

**✅ Clarified Assumptions:**
- Only lowercase English letters
- Inputs are valid and non-null
- Length mismatch immediately disqualifies anagrams

---

### 🔬 2. Examples & Edge Cases

**Given Example:**  
`"anagram"` and `"nagaram"` → ✅ True  
`"rat"` and `"car"` → ❌ False

**Custom Edge Cases:**  
- `("", "")` → ✅ True (empty strings are trivially anagrams)  
- `("a", "a")` → ✅ True  
- `("ab", "a")` → ❌ False (different lengths)  
- `("a"*100000, "a"*99999 + "b")` → ❌ False (length match but count mismatch)

---

### 💡 3. Brainstorm Solutions

**Brute Force:**
> "We could sort both strings and compare them. If they match, they’re anagrams."

- Time: `O(n log n)`
- Space: `O(n)` (for sorted copies)
- ✅ Simple but not optimal

**Better Approach: Hashmap (or Array Counter):**
> "Since we only care about 26 lowercase letters, we can use an array of size 26 as a fixed character frequency counter. One string increments, the other decrements."

> "If all counts return to 0, they cancel each other out — like a slider moving left/right. If any count is nonzero at the end, the strings differ."

- Time: `O(n)`
- Space: `O(1)` (fixed 26-size array)

✅ Best for this input domain  
🧠 Mention that you would use hashmaps if the input were Unicode or case-sensitive.

---

### 🧱 4. Implementation Plan (Talk Through Before Typing)

1. Check if `len(s) != len(t)` → return False immediately
2. Initialize `count = [0] * 26`
3. Loop through both strings in one pass:
    - Increment for `s[i]`
    - Decrement for `t[i]`
4. After loop, check if all values in `count` are zero
5. If yes, return True. Else, return False.

Use:  
```python
ord(char) - ord('a')
```
To convert letters to array indices.

---

### 🧠 5. Code Complexity Analysis

- **Time Complexity:** `O(n)` – One full pass over both strings
- **Space Complexity:** `O(1)` – Fixed-size array for 26 characters

---

### 🔍 6. Final Review & Wrap-Up

> “My solution is clean, works in linear time, and avoids hashmaps since we’re limited to lowercase letters.”
>
> “If the input were Unicode or included other characters, I’d switch to a dynamic hashmap-based counter.”

> “Would you like me to walk through test cases or show the sorting-based version as a backup?”

✅ Confident ending. Always offer next steps or ask the interviewer if they want further discussion.
