class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        tar = ord(target) - 97
        
        for k in letters :
            if (ord(k)-97) > tar:
                return k

        return letters[0]

