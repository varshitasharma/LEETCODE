class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length, max_area = len(heights), 0
        increasing_stack = [-1]
        for i in range(length+1):
            while(increasing_stack[-1] != -1 and (i == length or heights[increasing_stack[-1]] > heights[i])):
                curr_height = heights[increasing_stack[-1]]
                increasing_stack.pop()
                left_smallest, right_smallest = increasing_stack[-1] + 1 , i-1
                max_area = max(max_area, (right_smallest - left_smallest +1)*curr_height)
                            
            increasing_stack.append(i)
        return max_area
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            