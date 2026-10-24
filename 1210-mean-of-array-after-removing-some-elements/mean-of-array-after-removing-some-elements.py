class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n  = len(arr)
        k = n // 20

        return sum(arr[k:n-k])/(float)(n-2*k)