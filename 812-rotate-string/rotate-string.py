
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        combined = s + s

        n = len(combined)
        m = len(goal)

        for i in range(n - m + 1):

            match = True

            for j in range(m):

                if combined[i + j] != goal[j]:
                    match = False
                    break

            if match:
                return True

        return False
