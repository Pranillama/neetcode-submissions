'''
Understand:
- given: arrary (nums) -> ascending order, possibly been rotated 
- Find, the Target in that (nums) -> if not then retuen (-1)

- every #'s in nums must be unique
- **TARGET = IDEXE**

Plan:
- Brute Force: going throuh all the arrays using nested loop (i & j) and finding the target

- Binary search:
- we need l and r pointer 
- while, l < r -> mid = l+r//2 

- HOW TO KNOW WHICH PART TO NEGLECT?
- compare (mid <= r) -> if yes, does my (t) lies betw mid & r? -> we move l = mid+1
- if not, do the same thing (is ascending? does t lie betw mid & r?)

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        t = target

        while l <= r:
            mid = (l + r) // 2

            # NEED THIS AS WHAT IF MID = T, 
            if nums[mid] == t:
                return mid

            if nums[mid] <= nums[r]:
                if nums[mid] < t <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= t < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1


# time: (log n), space o(n)






        