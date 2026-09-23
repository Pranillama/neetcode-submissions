'''
Understanding:
- It's like a security: Input -> encode(str) -> pass it to a  decoder(str) -> Output
- Input = Output
- my understanding: Encoder => ['we','are','happy'] -> ["wearehappy"]

- is it all string? or other char's as well? = yes all ASCII char, #'s all

Plan:
- Brute force: we could have used a non-ASCII char like emoji or som shit for delimiter(takes a lot of space)

- HOW WILL DECODER KNOW THE SPACE OR WORD IN COMBINED STRING?

- take the list of strings
- encoder -> we use a (No & #) as a delimiter -> encode
- the encode -> decoder (reads the No at front of the # and knows the exact number of string) -> store it as strings in an array
- return that array
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # "Hello" => 5#Hello
            res += str(len(s)) + "#" + s 
        return res

# i and j are pointers we use
    def decode(self, s: str) -> List[str]:
        res =[]
        i = 0 # start from the index O

        while i < len(s):
            j = i # put j in the same position as i

            while s[j] != "#": # if j is not # bring then there
                j += 1
            # extract the length of the comming string. i(number) starting from j
            length = int(s[i:j]) 

            res.append(s[j + 1: j + 1 + length]) #extract the lenght and add

            i = j + 1 + length #move i forward to the next No where the j is also.

        return res
            


