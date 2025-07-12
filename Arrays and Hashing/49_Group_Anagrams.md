## Summary
- Use a **hashmap** to group words by a shared key  
- Two common signatures:
  - **Sorted string** (e.g., "eat" → "aet")
  - **Char count tuple** (26-length array for a–z → tuple)

**Best Solution: Hashmap with char count tuple**  
- For each word, count how often each of the 26 letters appears  
- Use the count tuple as the key, and append the word to the value list

## [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
**Precondition:** Any known constraints (e.g., "only lowercase letters", "no negative numbers")

> 💡 Short explanation of what the problem is actually testing

---

### Approach 1: Sorting each word  
**Time Complexity:** `O(m * nlogn)`  
> n = avg length of input strings, m = # of strings

**Space Complexity:** `O(m * n)`  
**Idea:** Sort each word alphabetically — anagrams will have the same sorted form.  
Use the sorted word as a hash table key to group original words.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)  
        for s in strs:
            sortedS = ''.join(sorted(s)) # this will be our key
            res[sortedS].append(s) # append word to the list at key
        return list(res.values()) # return just the values
```

**Notes:**
```python
res = defaultdict(list)
```
> use defaultdict so if a key (the sorted string) DNE, a new list is auto created for that key, avoiding the need to check if the key exists before appending

```python
sortedS = ''.join(sorted(s))
```
> sort each string alphabetically and join it back into a new string — this becomes the key.  
> all anagrams will have the **same sorted form**, so they'll group under the same key.

```python
res[sortedS].append(s)
```
1. Use the sorted version of the string as the key  
2. Append the original string to the list at that key

```python
return list(res.values())
```
We just return the grouped anagram lists, not the keys.

So `res` looks like:
```python
{
  "aet": ["eat", "tea", "ate"],
  "ant": ["tan", "nat"],
  "abt": ["bat"]
}
```

`res.values()` becomes:
```python
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]
```

**Example:**
input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
```css
Word: 'eat' → Sorted Key: 'aet'
Current Groups: { 'aet': ['eat'] }

Word: 'tea' → Sorted Key: 'aet'
Current Groups: { 'aet': ['eat', 'tea'] }

...

Final Anagram Groups: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```


---

### Approach 2: Hash Table
**Time Complexity:** `O(m*n*26)` 
> n = avg length of input strings, m = # of strings, a-z(26) length of count array

**Space Complexity:** `O(?)`  
**Idea:** Count the frequency of each character (a-z) in each word.  
Use the tuple of counts as a hashable key to group anagrams, since anagrams share the same letter frequencies.


```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #for edge case. this is a  dictionary where each value is a list. 
        for s in strs:
            count = [0] * 26 # create 26-element list as a counter for each char in the alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1 #increment count for correct letter based on ASCII value
# last two lines groups each word by character count signature, and returns all grouped list of anagrams
            res[tuple(count)].append(s) # tuple immutable --> use as dictionary key
        return list(res.values())
```
**Notes: **
```python
res = defaultdict(list)
```
> use defaultdict so if a key/tuple(count) DNE, a new list is auto created for that key, avoiding the need to check if key exists before appending

```python 
res[tuple(count)].append(s)
``` 
  ```tuple(count)``` converts the lists to a tuple. Since Tuples are **immutable**, they can be used a dict keys. 

```python 
res[tuple(count)].append(string)
```
  1. Use tuple of character counts as key,
  2. append original string to that group (the value list)

```python
return res.values()
```
Anagrams groups will be sorted like this in res: 
```python
{
  (1, 0, 0, ..., 1): ["at", "ta"],
  (0, 1, 1, ..., 0): ["bat"],
  ...
}
```
We just return the list of anagrams, not frequency keys
So ```res.values()```:
```python
[
  ["at", "ta"],
  ["bat"],
  ...
]

```

**Example:**
input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
```css
Word: 'eat' → Count Key: (1, 0, ..., 1, ...)
Current Groups: { (1, ..., 1): ['eat'] }

Word: 'tea' → Count Key: ...
Current Groups: { ... (1, ..., 1): ['eat', 'tea'] }

...

Final Anagram Groups: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```


---

### Notes
- What you learned
- Any mistakes you made or edge cases you missed
- Patterns to remember for similar problems


---

### 🧠 Concept Check: Why Tuples Work as Hash Table Keys (and Lists Don’t)

```python
res[tuple(count)].append(s)
```

🔒 **Why not just use `count` (a list) as a key?**

- Python requires **dictionary keys to be hashable**.
- A key must return a **consistent hash value** — i.e., `hash(key)` must never change.
- Lists are **mutable** → they can be modified after creation → their hash would change → ❌ unsafe as keys.
- Tuples are **immutable** → their hash is fixed and consistent → ✅ safe for hash table keys.

---

🧠 **If mutable keys were allowed**, your program could lose track of data.  
Imagine:

```python
lst = [1, 2, 3]
my_dict = {lst: "value"}  # ❌ TypeError: unhashable type: 'list'
```

If `lst[0] = 9`, then:
- Its hash would change
- Python would lose track of the original key → broken dictionary behavior

---

✅ **Takeaway:**
- Use `tuple()` to convert mutable data (like a list of character counts) into a safe, hashable format.
- This lets you group anagrams reliably using frequency patterns.

