class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []

        for k in address :
            if k == ".":
                result.append("[.]")
            else :
                result.append(k)

        return "".join(result)