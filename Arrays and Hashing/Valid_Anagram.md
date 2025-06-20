## 242. Valid Anagram [link](https://leetcode.com/problems/valid-anagram/)
**Precondition:** Anagrams are the same length in characters
We will always check this first

### Sorting
**Time: O(nlogn + mlogm)**
**Space: O(1) or O(m+n)** depending on sorting algo
```python
if len(s) != len(t):
	return False
	
return sorted(s) == sorted(t)
```
> Anagrams just means two words have the same number of specific characters
> 
> Letters have underlying ascii values, so if we can get those letters or values in the same order we can quickly check if they are equal


### Hashmap