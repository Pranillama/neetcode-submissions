'''
Understanding:
- array of #'s -> output = product of all the #'s instead of the index(i), it's currently in
- the product can't be greater than 2^32 <<

- output can be in any order?

Plan:
- Brute force: iterate through all the num[i] -> find product of #'s beside the index, time: o(n2)=> i(outer loop), j(inner loop to calculate the product)

- prefix and suffix (Left / Right):
- Left Array: move the (i) to -> Right = calculating the left multiplier
- At the same time;
- Right Array: move the (j) to -> Left = calculating the right multiplier
- Final output = [left[l] * Right[r]]

Time: o(n), why? because both i and j are moving at the same time not a double loop.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)

        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1 # moving from the oposite direction of i
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        return [ l*r for l,r in zip(l_arr, r_arr)] # multiply each index in i(left) and j(right) -> return list

        #Time: o(n) = as i and j is iterating same time from front & back
        #space: o(n) = grows as input



        