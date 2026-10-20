class Solution(object):
    def runningSum(self, nums):
        sumi = []

        for i in range(len(nums)) :
            sumi.append(sum(nums[:i+1]))
    
        return sumi