from collections import deque

class Solution(object):

    # Queue Simulation:
    # Directly simulates the problem's behavior using a deque.
    # Time: O(n^2) — for each sandwich, we may rotate through the entire queue.
    # Space: O(n) — the deque grows with the number of students.
    def Queue(self, students, sandwiches): 
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

    # Iterative Index Solution:
    # Uses an index to simulate a circular queue without extra structures.
    # Time: O(n^2) — same logic, nested loop.
    # Space: O(1) — no additional data structures used.
    def IterativeCountStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
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

    # Optimal HashMap Solution:
    # Track how many students prefer each sandwich type.
    # A sandwich can only be served if someone wants it.
    # Time: O(n) — one pass for counting, one for serving.
    # Space: O(1) — only two keys (0 and 1), so space stays constant.
    def frequencyCountStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
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
