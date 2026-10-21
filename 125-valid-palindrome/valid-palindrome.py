class Solution(object):
    def isPalindrome(self, s):
        
        cleaned=""

        for i in s.lower():
            if i.isalnum():
                cleaned += i

        if cleaned[:] == cleaned[::-1]:
            return True
        else :
            return False

