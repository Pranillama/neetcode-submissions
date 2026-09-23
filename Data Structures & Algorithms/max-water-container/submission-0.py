'''
Understanding:
- need to return the max water that the container can store
- max water = max (h * w)
- h = min(h1,h2), w = diff btw 2 ith bar

- what if only one # ? -> no container
- can the hights be greater than n?

Plan:
- brute force: go through all the bars(int) in the array -> calcualte the max water -> compare it -> time: On2

- 2 pointer left & right 
- calcualte the max water = (j-i) * min(height[i],height[j]) -> max water ->
- move the small pointer inward by one position -> calculate max water
- if it's larger (current > max water) then we update the store

'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right: # meet in the middle
            # calculate the current area
            current_width = right - left
            current_height = min(heights[left], heights[right])
            current_area = current_width * current_height

            # update the max water:
            max_water = max(max_water, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return max_water

# time: O(n), space: O(1)



