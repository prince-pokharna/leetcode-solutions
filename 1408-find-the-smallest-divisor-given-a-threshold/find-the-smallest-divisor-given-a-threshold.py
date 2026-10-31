class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right :
            mid = (left+right) //2
            sum = 0

            for num in nums:
                sum += -(-num//mid)

            if sum <= threshold :
                right = mid
            else:
                left = mid + 1

        return left

