class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = {}

        for x in magazine :
            freq[x] = freq.get(x,0) + 1

        for y in ransomNote :
            if freq.get(y,0) == 0 :
                return False
            
            freq[y] -= 1
        
        return True
         