class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi = 0
        count = 0

        for i in nums:
            if i == 1:
                count += 1
                maxi = max(count, maxi)
            else :
                count = 0
        
        return maxi