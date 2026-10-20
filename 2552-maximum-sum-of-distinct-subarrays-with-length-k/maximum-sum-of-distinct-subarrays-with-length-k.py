class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen = set()
        left = 0
        total = 0
        maxi = 0

        for right in range(len(nums)):

            while nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1

            seen.add(nums[right])
            total += nums[right]

            if right - left + 1 == k:
                maxi = max(maxi, total)

                seen.remove(nums[left])
                total -= nums[left]
                left += 1

        return maxi