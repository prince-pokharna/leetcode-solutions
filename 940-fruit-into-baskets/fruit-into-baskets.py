class Solution(object):
    def totalFruit(self, fruits):
        maxi = 0
        seen = {}
        left = 0

        for right in range(len(fruits)):
            seen[fruits[right]] = seen.get(fruits[right], 0) + 1

            while len(seen) > 2:
                seen[fruits[left]] -= 1

                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi