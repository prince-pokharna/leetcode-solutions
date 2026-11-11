class Solution:
    def countAndSay(self, n):
        s = "1"

        for _ in range(n - 1):
            result = []
            i = 0

            while i < len(s):
                j = i

                while j < len(s) and s[j] == s[i]:
                    j += 1

                count = j - i

                result.append(str(count))
                result.append(s[i])

                i = j

            s = "".join(result)

        return s