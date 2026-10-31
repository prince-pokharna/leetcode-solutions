from math import isqrt

class Solution(object):
    def pivotInteger(self, n):
        total = n * (n + 1) // 2
        mid = isqrt(total)

        if mid * mid == total:
            return mid

        return -1