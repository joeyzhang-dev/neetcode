## Summary
- Check if lengths match (early exit — anagrams must be same length) 
**Best Solution**
- hashmap to count each char in str1, decrement for str2
**Two Hashmap Solution:**   
- Build two hashmaps: `char → freq`, then compare keys and values
- Use a Hashmap array

## 242. Valid Anagram [link](https://leetcode.com/problems/valid-anagram/)
**Precondition:** Anagrams are the same length in characters
We will always check this first

> Anagrams just means two words have the same number of specific characters


### Sorting
**Time: O(nlogn + mlogm)**
**Space: O(1) or O(m+n)** depending on sorting algo
```python
if len(s) != len(t):
	return False
	
return sorted(s) == sorted(t)
```

> Letters have underlying ascii values, so if we can get those letters or values in the same order we can quickly check if they are equal


### Hashmap
**Time: O(S+T)**
**Space: O(1)** since we have at most 26 different characters
Using two Hasmaps we can track the # of each characters for both words then we compare to see if the conditions of a true anagram are met
**Hashmap** = Letter:Occurrences 
```python
if len(s) != len(t):
	return False
countS, countT = {}, {}
for i in range(len(s)): # fill in the two hashmaps
	countS[s[i]] = 1 + countS.get(s[i], 0) #.get has default value in case not initialized
	countS[t[i]] = 1 + countS.get(t[i], 0)
for c in countS: # check all the counts are the same
	if countS[c] != countT.get(c,0): # .get again in case character mismatch 
		return False # return false immediately t
return True

```

### HashTable using Array
**Time: O(n+m)**
**Space: O(1)**
If input is **only lowercase** letters

```python

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