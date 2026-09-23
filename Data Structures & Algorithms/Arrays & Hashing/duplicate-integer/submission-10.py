'''
Understand:
- true: if a value in the array appear more than once
- false: if none

plan:
brute force: arrance in acending order -> then check each elements with another one at a time
Hash set: set doesn't allow duplicates -> add elements in set -> if duplicate then "true"
or HashMap
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #empty set
        for num in nums:
            if num in seen:
                return True
            seen.add(num) # .add as set is unordered so can be added anywhere unlike .append
        return False
        