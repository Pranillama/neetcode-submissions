'''
Understanding:
- given arrray and target (t)
- 2 #'s that sums to the target t
- it is in ascending order

- i != j
- there is a pair in every condition


Plan:
Brute force: loop over each number using nested loopand try to find the sum between. time: O(n2), space:O(n)

- Hash map:
- take the first # subtract it with the t -> add that difference to value 
- then we move to the next number -> see if it is present in the hash map or not 
- If it is -> found pair 
- If not -> we repeate
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff],i]

            # other wise add the number to the key
            seen[n] = i


        