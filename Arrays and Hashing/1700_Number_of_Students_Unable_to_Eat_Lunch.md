## Summary
- Use a **queue simulation** or **frequency counting** approach
- Key insight: track student preferences and serve sandwiches in order
- Early exit when no students want the current sandwich

**Best Solution: Frequency counting**  
- Count student preferences, serve sandwiches in order, track remaining students

## [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)
**Precondition:** Students and sandwiches arrays have same length, values are 0 or 1

> 💡 Simulate a lunch queue where students take sandwiches they prefer, or leave if they don't want the current sandwich

---

### Approach 1: Frequency Counting (Optimal)
**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)` (only two keys: 0 and 1)  
**Idea:** Count how many students prefer each sandwich type, then serve sandwiches in order and track remaining students.

```python
def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    result = len(students)
    count = {}  # preference count: {0: num, 1: num}

    # Count preferences
    for s in students:
        if s not in count:
            count[s] = 0
        count[s] += 1

    # Serve sandwiches
    for s in sandwiches:
        if count.get(s, 0) > 0:
            result -= 1
            count[s] -= 1
        else:
            return result  # no one wants this sandwich

    return result
```

> 🧠 Most efficient approach. We only need to count preferences once, then serve sandwiches in order. Early exit when no students want the current sandwich.

---

### Approach 2: Queue Simulation
**Time Complexity:** `O(n²)`  
**Space Complexity:** `O(n)`  
**Idea:** Directly simulate the problem using a deque. Rotate students until we find one who wants the current sandwich.

```python
from collections import deque

def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    n = len(students)
    q = deque(students)
    res = n  # total hungry students at the start

    for sandwich in sandwiches:
        count = 0  # tracks how many students we've checked

        # Rotate the queue until we find a matching student or check all
        while count < n and q[0] != sandwich:
            q.append(q.popleft())
            count += 1

        if q and q[0] == sandwich:
            q.popleft()
            res -= 1
        else:
            break  # No student wants this sandwich

    return res
```

> 🧠 Direct simulation of the problem. Less efficient due to queue rotations, but very intuitive to understand.

---

### Approach 3: Iterative Index Solution
**Time Complexity:** `O(n²)`  
**Space Complexity:** `O(1)`  
**Idea:** Use an index to simulate a circular queue without extra data structures.

```python
def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    n = len(students)
    index = 0
    result = n  # number of hungry students

    for sandwich in sandwiches:
        count = 0

        # Scan for a student who wants this sandwich
        while count < n and students[index] != sandwich:
            index = (index + 1) % n  # wrap around like a circular queue
            count += 1

        if students[index] == sandwich:
            students[index] = -1  # mark as served
            result -= 1
        else:
            break  # no one left wants this sandwich

    return result
```

> 🧠 Space-efficient approach that modifies the original array. Uses modulo to simulate circular queue behavior.

---

### Test Cases
```python
# Example test cases
assert countStudents([1,1,0,0], [0,1,0,1]) == 0
assert countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3
```

---

### Notes
- Frequency counting is optimal for most cases
- Queue simulation is most intuitive but less efficient
- All approaches handle edge cases correctly
- The key insight is that we can stop serving when no students want the current sandwich
- Remember that students can only take sandwiches from the top of the stack 