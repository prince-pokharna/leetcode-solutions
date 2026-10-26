class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0

        for k in stones :
            if k in jewels:
                count +=1
        return count
        