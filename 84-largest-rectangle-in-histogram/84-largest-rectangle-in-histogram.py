class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0) #Add dummy height so that when you reach last actual height, you have next index to compare it with
        stack = [-1] 
        # Add -1 so that you include left index as 0 for case when all elements to the left of current right were greater than that. So all elements would have got popped according to while condition. So left index must be equal to zero to get the width -> stack[top] must be equal to -1 -> to get left = 0 (-1 + 1)
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]: # pop until prev height > currheight
                height = heights[stack.pop()] 
                width = i - stack[-1] - 1 # right = i-1, left = stack[-1]+1, width = right-left+1
                ans = max(ans, height * width)
            stack.append(i)  # push current index to stack
        heights.pop()
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            