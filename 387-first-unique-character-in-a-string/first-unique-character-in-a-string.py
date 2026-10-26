class Solution(object):
    def firstUniqChar(self, s):
        seen = {}

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i

        return -1