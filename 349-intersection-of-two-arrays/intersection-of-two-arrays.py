class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        result = set()

        for i in nums2 :
            if i in seen :
                result.add(i)
        
        return list(result)