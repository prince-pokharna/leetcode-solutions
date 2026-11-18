class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        result = ""

        for ch in s:
            freq[ch] = freq.get(ch , 0) + 1

        for ch in order :
            if ch in freq :
                result += ch * freq[ch]
                del(freq[ch])

        for ch , count in freq.items():
            result  += ch *count

        return result