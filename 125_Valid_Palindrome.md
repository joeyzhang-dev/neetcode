## 📋 Table of Contents

- [🧠 Summary](#-summary)
- [📄 Problem Statement](#-problem-statement)
- [🔎 Approach 1: Brute Force with Filter + Reverse](#-approach-1-brute-force-with-filter--reverse)
- [⚙️ Approach 2: Two Pointer In-Place](#-approach-2-two-pointer-in-place)
- [🔁 Two Pointer Diagram Walkthrough](#-two-pointer-diagram-walkthrough)
- [📚 DSA Concepts Explained](#-dsa-concepts-explained)
- [🧪 Test Cases](#-test-cases)
- [🧱 Interview Walkthrough (CLEAN)](#-interview-walkthrough-clean)
---

## 🧠 Summary

- Determine if a string is a palindrome considering only alphanumeric characters and ignoring cases.
- ✅ Clean the input to remove non-alphanumerics.
- ✅ Use a two-pointer strategy to compare characters from both ends efficiently.
- Brute force creates a cleaned string and compares it to its reverse.
- Two-pointer avoids extra space by checking in-place.

**Best Solution:** Two Pointer  
- Space-efficient and avoids string reconstruction — ideal for large inputs.

---

## 📄 Problem Statement

> Given a string `s`, return `true` if it is a palindrome, or `false` otherwise. Only consider alphanumeric characters and ignore cases.

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- Only ASCII characters

---

## 🔎 Approach 1: Brute Force with Filter + Reverse

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]
```

> 🧠 Clean and simple — but builds a new filtered string and reversed version in memory. Fine for short inputs but not space-optimal.

---

## ⚙️ Approach 2: Two Pointer In-Place

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)` (ignoring input string space)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
```

> 🧠 Checks characters on-the-fly without creating new strings — this is optimal for large or streamed input.

### 🔁 Two Pointer Diagram Walkthrough

Input:  
```
"A man, a plan, a canal: Panama"
```

We'll show the positions of the left (`^`) and right (`^`) pointers at each step:

---

#### Step 1: Compare 'A' and 'a' ✅
```
A man, a plan, a canal: Panama
^                             ^
l                             r
```

---

#### Step 2: Skip ' '  
```
A man, a plan, a canal: Panama
  ^                           ^
  l                           r
```

#### Step 3: Compare 'm' and 'm' ✅
```
A man, a plan, a canal: Panama
  ^                         ^
  l                         r
```

---

#### Step 4: Compare 'a' and 'a' ✅
```
A man, a plan, a canal: Panama
    ^                     ^
    l                     r
```

---

#### Step 5: Compare 'n' and 'n' ✅
```
A man, a plan, a canal: Panama
     ^                 ^
     l                 r
```

---

#### Step 6: Skip ',' and ' '  
```
A man, a plan, a canal: Panama
        ^           ^       
        l           r
```

#### Step 7: Compare 'a' and 'a' ✅
```
A man, a plan, a canal: Panama
        ^         ^
        l         r
```

---

#### Step 8: Compare 'p' and 'p' ✅
```
A man, a plan, a canal: Panama
         ^       ^
         l       r
```

---

#### Step 9: Compare 'l' and 'l' ✅
```
A man, a plan, a canal: Panama
           ^   ^
           l   r
```

---

#### Step 10: Compare 'a' and 'a' ✅
```
A man, a plan, a canal: Panama
            ^ ^
            l r
```

---

#### Pointers Cross → Done ✅  
Every comparison matched → `True` ✅

---

> 🧠 This shows how the two-pointer method compares only valid alphanumerics and skips everything else — case-insensitively.



## 📚 DSA Concepts Explained

<details>
<summary>🔹 Two Pointer Technique</summary>

Move two indices inward from both ends of the input. Useful when checking symmetric properties (like palindromes) or when minimizing space by avoiding new strings/lists.

</details>

<details>
<summary>🔹 String Filtering with `isalnum()`</summary>

The `str.isalnum()` method checks if a character is alphanumeric (a-z, A-Z, 0-9). It's used to ignore punctuation and spaces during comparison.

</details>

<details>
<summary>🔹 Case Normalization</summary>

Use `str.lower()` (or `str.upper()`) to standardize characters before comparison to make the algorithm case-insensitive.

</details>

(Add more as needed)


---

## 🧪 Test Cases

```python
sln = Solution()

# Basic palindrome
assert sln.isPalindrome("A man, a plan, a canal: Panama") == True

# Not a palindrome
assert sln.isPalindrome("race a car") == False

# Empty string
assert sln.isPalindrome("") == True

# Only special characters
assert sln.isPalindrome("!!!") == True

# Palindrome with mixed cases and symbols
assert sln.isPalindrome("No 'x' in Nixon") == True

# One alphanumeric character
assert sln.isPalindrome("Z") == True

# Alphanumeric but not a palindrome
assert sln.isPalindrome("0P") == False
```


---

## 🧱 Interview Walkthrough (CLEAN)

---

### 🔍 1. Clarify

> 🧑‍💼: “Given a string `s`, return `True` if it is a palindrome — ignoring non-alphanumeric characters and case. Otherwise, return `False`.”

**✅ Clarified Assumptions:**
- Input may include letters, digits, spaces, punctuation.
- Case should be ignored (e.g., 'A' == 'a').
- Empty strings and strings with only symbols (like `"!!"`) should return `True` by definition.
- Only ASCII characters (no Unicode or emojis).

> Me: “Got it. So I'm checking whether the input is a palindrome when filtered down to only alphanumeric characters and ignoring casing. For example, `"A man, a plan, a canal: Panama"` should return `True`, correct?”

> 🧑‍💼: “Exactly.”

---

### 🔬 2. Examples

**🧪 Provided Example:**

```python
Input: "A man, a plan, a canal: Panama"
Output: True
```

**🧪 Custom Example 1 (non-palindrome):**
```python
Input: "race a car"
Output: False
```

**🧪 Custom Example 2 (edge case):**
```python
Input: "!!!"
Output: True
# Only symbols — after filtering it's empty, which counts as a palindrome.
```

**🧪 Custom Example 3:**
```python
Input: "0P"
Output: False
# '0' and 'P' are not equal
```

---

### 💡 3. Brainstorm

**🪫 Brute Force Idea:**
- Filter the string to keep only alphanumeric characters
- Convert all characters to lowercase
- Check if the filtered string is equal to its reverse

**Time:** O(n)  
**Space:** O(n) for new string

**⚡ Optimized Idea (Two Pointer):**
- Use two pointers: one from the start, one from the end
- Skip non-alphanumeric characters
- Compare lowercase versions of characters
- Return False if any mismatch

**Time:** O(n)  
**Space:** O(1) extra (in-place comparison)

> 🧑‍💼: “Which approach would you like to go with?”

> Me: “Let me implement the brute force one first since it’s fast and readable. Then I’ll optimize to the two-pointer version for space efficiency.”

---

### 🧰 4. Plan

**Step-by-step:**

**Brute Force Plan:**
1. Create a list of lowercase characters from `s` where `c.isalnum()` is true.
2. Compare that list to its reversed version.

**Two Pointer Plan:**
1. Initialize two indices: `l = 0`, `r = len(s) - 1`
2. While `l < r`:
   - Skip `s[l]` if not alphanumeric
   - Skip `s[r]` if not alphanumeric
   - Compare `s[l].lower()` to `s[r].lower()`
   - If mismatch → return False
   - Else → move inward
3. If loop completes, return True

---

### 🧠 5. Complexity

| Approach       | Time       | Space      |
|----------------|------------|------------|
| Brute Force    | O(n)       | O(n)       |
| Two Pointer    | O(n)       | O(1)       |

- `n` is the length of the input string
- Both scan every character at most once
- Two-pointer is more memory-efficient since it avoids building a new string

---

### ✅ 6. Wrap-up

✅ The brute-force method is simple and readable for interviews.  
✅ The two-pointer solution is optimal for space and demonstrates string parsing logic.  
✅ Edge cases like empty strings, single characters, or only symbols are handled.  
✅ The solution avoids using regex or libraries, sticking to core string methods.

> Me: “Let me know if you'd like me to walk through another variant — like full Unicode handling or ignoring diacritics.”



