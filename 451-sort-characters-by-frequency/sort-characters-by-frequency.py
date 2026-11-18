
class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        arr = list(freq.items())

        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if left[i][1] >= right[j][1]:
                    result.append(left[i])
                    i += 1

                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        sorted_freq = merge_sort(arr)
        answer = ""

        for ch, count in sorted_freq:
            answer += ch * count

        return answer
