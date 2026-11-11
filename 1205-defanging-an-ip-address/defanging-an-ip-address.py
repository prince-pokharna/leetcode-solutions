class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""

        for k in address:
            if k == ".":
                result += "[.]"
            else :
                result +=k

        return result