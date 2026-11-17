class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0

        for i in range(len(word)):
            freq = {}

            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break

                freq[word[j]] = freq.get(word[j], 0) + 1

                if len(freq) == 5:
                    count += 1

        return count
