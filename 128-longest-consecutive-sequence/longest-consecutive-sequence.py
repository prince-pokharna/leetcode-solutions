class Solution(object):
    def longestConsecutive(self, nums):
        seen = set(nums) #O(1)
        max_len = 0

        for k in seen :
            if k-1 not in seen :
                count = 1
                current = k

                while current+1 in seen :
                    current +=1
                    count +=1

                max_len = max(max_len , count)

        return max_len
