class Solution(object):
    def isAnagram(self, s, t):
        if(len(s) != len(t)):
            return False

        freq = {}

        for x in s :
            freq[x] = freq.get(x, 0) + 1

        for y in t :
            freq[y] = freq.get(y, 0) - 1
        
        return all(value == 0 for value in freq.values())