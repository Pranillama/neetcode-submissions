'''
Understanding:
- we hvae an array: can have multiple duolicate #'s &interger k
- e.g [1,2,2,3,3,3,4,4], k=2 -> [2,3] ->return the k most frequent(no order)

- the result should be unique, can't be the same # -> it's not the senario in this question.
- if no frequent no e.g. [1,2,3] then?
- will it be sorted?

Plan:
Brute force: go through each #'s in arrary -> use hashmap to store the # as keys/values(how many times) -> arrange that dict to "decending order" based on the frequency -> return the first k element
time: O(n) for hashmap, mlogn for sort

- Use Buket sort: as sorting is O(n) as uses insertion sort itself inside
- we make the hash map(key,value) using counter
- make a buckets with n+1 : n+1 as we need for freq 0 as well -> make all of the items in the buket 0
- then we add the #'s "as lists" in the designated buckets
- eventually if we read it from backwards -> its going to be decending order
- we pick the k #'s -> then merge it if its seperate

time: O(n) -> as no sorting, space: O(n)

-
'''
# counter: automatically counts the freq of the #'s in list,tuple,dictionay -> and place it in an hash/dict as key and value it self
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n =len(nums)
        counter = Counter(nums) 
        buckets = [0] * (n+1) # we need Extra place for 0 frequency

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] =[num] # we add them as a list in buckets so that we can add #'s later
            else:
                buckets[freq].append(num)

        ret = []
        for i in range(n, -1, -1): # (for n #, we come from back, one at a time)
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        return ret





#Bucket sort: https://www.youtube.com/watch?v=xeT31rm3bN0&vl=en
#This problem: https://www.youtube.com/watch?v=phNDYf1xzco&t=787s

        