class Solution(object):
    def findMaxAverage(self, nums, k): 
       current_sum = sum(nums[:k])
       maxi = current_sum
       left = 0


       for right in range(k, len(nums)):
            current_sum += nums[right] - nums[left]
            maxi = max(maxi, current_sum)
            left +=1

       return maxi/float(k) 



         
