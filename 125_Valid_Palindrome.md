## 📋 Table of Contents

- [🧠 Summary](#🧠-summary)
- [📄 Problem Statement](#📄-problem-statement)
- [🔎 Approach 1](#🔎-approach-1)
- [⚙️ Approach 2 (if any)](#⚙️-approach-2-if-any)
- [📚 DSA Concepts Explained](#📚-dsa-concepts-explained)
- [🧪 Test Cases](#🧪-test-cases)
- [🧱 Interview Walkthrough (CLEAN)](#🧱-interview-walkthrough-clean)
- [❌ Common Pitfalls](#❌-common-pitfalls)
- [📚 Glossary](#📚-glossary)

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

(Add more as needed)

---

## 🧪 Test Cases

```python
assert Solution().fn(...) == ...
# Add diverse edge and normal cases
```

---

## 🧱 Interview Walkthrough (CLEAN)

### 🔍 1. Clarify

- Assumptions, input/output, edge cases

### 🔬 2. Examples

- Provided + 1-2 of your own

### 💡 3. Brainstorm

- Naive vs optimized ideas

### 🧰 4. Plan

- Step-by-step breakdown before coding

### 🧠 5. Complexity

- Time and space discussion

### ✅ 6. Wrap-up

- Recap strengths, edge case coverage, invite follow-ups

---

## ❌ Common Pitfalls

- What people often get wrong
- Subtle edge cases or traps

---

## 📚 Glossary

| Term          | Meaning |
| ------------- | ------- |
| Hash Map      | ...     |
| Tuple         | ...     |
| Min Heap      | ...     |
| Frequency Map | ...     |


