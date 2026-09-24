'''
Understand: 
- return true => opening bracket is closed by -> same type, correct order, 
- return false => the stack not empty or when closing bracket only

- what if no opening bracket? just closing bracket.

Plan:
Brute force: for (i) search (j), iterate through -> time: o(n2)

Stack
- every brakets (push) -> STACK 
- if similar brackets in opposite direction then -> (pop) brakets
- if empty stack => true, else False
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        # hashmap to know close/open bracket
        hashmap = { 
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c not in hashmap: #opening bracket. as hashmap key -> closing bracket
                stack.append(c)
            else:
                if not stack: #if the stack is empty when we have closing btacket
                    return False
                else:
                    pooped = stack.pop()
                    if pooped != hashmap[c]: # if the opening is same as hashmap key(closing)
                        return False
        return not stack # check if the stack is empty or not

        # time:o(n), space: o(n)





        