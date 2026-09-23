"""
Understanding:
- anagram: having same char 
- find the anagram -> group them in list together
- return the list of strings of anagrams grouped together

- check the length of the anagram 
- if nothing then return empty
- check if lower case
- can there be more than 2 groups of anagram? -> yes


Plan:
- brute force: arrange the strings in the ascendding order and match them; for e.g. act, cat -> act,act = they are equal so anagram.
- time: O(n * mlogn) , space O(n)

- Same like regular anagram -> you can use a list of char(0-26) = as key ,
- values of that will be the strings
- caviate is that in python -> lists are mutable and can't be a hash so -> change the list to tuple
- time: O
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # default dict = as if no key also it won't crash, which would in regular dict
        for s in strs: #n
            count = [0] * 26 # make the list a...z

            for c in s: #m
                count[ord(c) - ord('a')] +=1 # askey value of the c - a gives its position, then +1

            res[tuple(count)].append(s) #tuple as the lists can't be keys in hashmap

        return list(res.values()) #return the list

# Time: (n * m), space: O(n)
# https://www.youtube.com/watch?v=eDmxPfVa81k
