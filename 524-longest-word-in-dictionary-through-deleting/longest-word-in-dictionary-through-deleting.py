class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        result = ""

        for word in dictionary :
            i = 0
            j = 0
            while i <len(word) and j < len(s):
                if word[i] == s[j]:
                    i+=1
                j+=1
                    
            if i == len(word):
                if len(word) > len(result) :
                    result = word
                elif len(word) == len(result) and word < result:
                    result = word

        return result 

        