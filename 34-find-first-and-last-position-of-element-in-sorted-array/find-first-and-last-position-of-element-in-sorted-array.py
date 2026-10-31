class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        inner = -1
        outer = -1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target :
                inner = mid 
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0  
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target :
                outer = mid 
                left = mid  + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [inner , outer]

        

                