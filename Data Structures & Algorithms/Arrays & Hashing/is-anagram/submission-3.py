'''
understand: 
 - anagram = each strings has the same character
 - 
 - strings has to match same length
 - no numbers or spaces in between

 plan:
 - brute force: Compare each char of each string one at a time -> O(n2), O(n)
 - array: we have a array of 26 char -> each char has 0 values -> then
 -> go through first string -> we add +1 in the char's seen in string 1
 -> then same thing with string 2 -> we subtract -1 for each char's
 -> if all char's in the array is 0, then its true, else false
or
Same thing with hash map:
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = []
        if len(s) != len(t):
            return False

        count = {} 
        for char in s:
            count[char] = count.get(char,0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

# time: O(n), space: O(1), as its linear

