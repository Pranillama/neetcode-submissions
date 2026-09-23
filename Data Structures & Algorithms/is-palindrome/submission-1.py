"""
Understanding:
- eg moom
- lowercase only?
- no numbers
- it has to have the same number of charecter

Plan:
- brute force: reading from left to right and addig in the array
- then again reading from right to left and matchin it.

- have a 2 pointer moving from either direction
- skip if it is a space or any other thing besides alphanumeric 
- else compare: If same then true if not false.
- then move both the pointer inwards and compare
- 

- string methods: .isalnum(), .lower(
- classes: a reusable blueprint or template for creating objects.uses functions and attribute.
- attribute: inside a class stores the variables data
-function (method): inside the class is the action that the class can take
)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right = 0, len(s) -1
        
        while left < right: 
            #if not a alphanum and other then ignore:+1 else same to right
            while left < right and not s[left].isalnum(): 
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left +=1
            right -=1

        return True
        
# time complexity: O(n)
# Space complexity: O (1)