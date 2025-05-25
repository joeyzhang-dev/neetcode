

class Solution(object):
  # best solution
    # For the sandwich to pop out the stack and the line to continue , there has to be at least one student that wants it
    # if there are no students left that want the sandwich then the remaining students are left hungry
  # Big O
    # Time complexity: O(n), O(n); We iterate through the students once to create the hashmap and another single pass through the sandwiches 
    # Space complexity: O(1); we created a hashmap but there are only two keys 
      # - no matter how many students there are, we are only using two memory slots or 'two bins'. only the value is changed, no new space is created
    
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
      result = len(students) # number of hungry students at beginning
      count = {} # creating empty hashmap (key:value)
      #In Python we can use count = Counter(students)
      for s in students: # loop of counter of student sandwich preferences
        if s not in count:
          count[s] = 0 # if preference hasn't been seen before, intialize and set count to zero
        count[s] += 1 # increment count for this preference

      for s in sandwiches: # loop through sandwiches
        if count[s] > 0: # we have at least one student willing to eat sandwich s
          result -= 1 # one less hungry student
          count[s] -= 1 # the student is fed so we don't worry about them anymore
        else: # no one wants this sandwich 
          return result 
          
      return result # number of hungry students at the end 
