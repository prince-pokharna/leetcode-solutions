class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        left = 0
        matched = 0
        result = ""
        min_len = float("inf")

        for ch in t :
            need[ch] = need.get(ch , 0 ) + 1

        
        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch , 0) + 1

            if ch in need and window[ch] <= need[ch]:
                matched += 1

            while matched == len(t):
                if right - left + 1 < min_len :
                    min_len = right - left + 1
                    result = s[left:right+1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    matched -= 1

                left +=1

        return result