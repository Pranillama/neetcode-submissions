"""
Understanding: 
- array: non decresing (incrementing)
- 1-indexed: means the starting # is 1 instead of 0

edge case:
- index 1 < index 2 & index 1 != index 2
- always 1 valid solution
- O(1)

Plan:
Brute force: take a # in an array and loop through the given array and try to find the pair -> time O(n^2), space O(logn)

hasmap: create a dictionary -> take a # from arrayy -> t - current # -> if that differnece is in the hash map then pair -> if not that that current # in hashmap -> Then we repeat it for another number. 
however, time O(n), space O(n)

two pointer: 
- we have a left pointer = index[0] and right pointer = index[n-1]
- add the point #, -> if sum > t,  then index[n-1] is large so -> to move left
- if sum < t, then to move the left pointed to the right side. 
- if found the sum = t to return
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right +1] # why +1? -> in this the index starts from 1 not 0 but we have started here left = 0.
            if current_sum > target:
                right -= 1
            else:
                left += 1

# time complexity: O(n) -> on each iteration at least one pointer moves
# space complexity O(1) -> We are just using a fixed value, the left - right pointers, and the current sum. These don't grow with the input size. not a list or dictionary
        