'''
Understand:
- given = array of n lenght (sorted in asecending order)
- its rotated betwen 1 to n times -> nums
- every n in mums are unique
- we return the minimum element in that nums

Plan:
Bruteforce: doing a linear search in the array (one at a time), time: o(n)

Using binary search to reduce the time.
- we have left (l)/right(r) pointers
- l+r // 2 -> mid point

- HOW WE KNOW TO TAKE LEFT OR RIGHT? -> here they are sorted and rotated so -> large will be in one side and the smaller will be on the other side

- Condition: \\just use 1 # to compare\\
nums [mid] > nums[r] -> we move to right (l = mid +1)
nums [mid] <= nums[r] -> we move to righ (r = mid -1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r: # based on pointers not nums
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid # move right pointer to mid as no need to see right half

        return nums[l]

    

        