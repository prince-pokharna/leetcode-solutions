class Solution(object):
    def moveZeroes(self, nums):
        right = len(nums)

        for left in nums :
            if left == 0 :
                nums.append(left)
                nums.remove(left)
        