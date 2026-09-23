'''
Understanding:
- from an array -> we return 3 #'s that ads to  == 0
- it can be in any order

- can not contain any duplicate = it can't have pairs of triplet thats same also can't be the same 'indeces' #
- it is a interger array (-ve & +ve)
- if no pairs then return empty 

Plan:
BRUTE FORCE: sort first [-4,-1,-1,0,1,2]-> for each i,j,k -> move each pair one at a time to the right (k then j then i) -> then add and see the value==0 or not -> this is 3 loops so  -> time: O(n3)

2 pointer:
- sort[-4,-1,-1,0,1,2] -> we take # with index (i)to be the target (t) 
-left pointer (j) = num(i+10 , right pointer(k)
- Then finding j+k == t, if (t > j+k/ t > 0=> move j right, if (t < 0/ t< j+k) => move k to left
- how to avoid duplicate? ->move j & k until j < k
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
        # if the below condition i.e. # > 0 or # == to previous # -> 
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip that number (to abovid duplicates)
#If besides these, then we skip the for loop and go down

            j = i + 1 # left
            k = len(nums) -1 # right
            
            target = -nums[i]
            while j < k:
                current_sum =  nums[j] + nums[k]

                if target > current_sum:
                    j +=1
                elif target < current_sum:
                    k -=1
                else: # target == current_sum 
                    result.append([nums[i], nums[j], nums[k]])
                    j +=1
                    # to avoid duplicates again
                    while j < k and nums[j] == nums[j-1]:
                        j +=1

        return result

#time: O(n), space: O(1)

            