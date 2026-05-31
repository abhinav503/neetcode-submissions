class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0 , len(height)-1
        leftMax, rightMax = 0, 0
        waterAccumulated = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >=  leftMax:
                    leftMax = height[left]
                else:
                    waterAccumulated += leftMax - height[left]
                left += 1
            else:
                if height[right] >=  rightMax:
                    rightMax = height[right]
                else:
                    waterAccumulated += rightMax - height[right]
                right -= 1
            print(waterAccumulated)

        return waterAccumulated