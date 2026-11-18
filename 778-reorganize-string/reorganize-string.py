import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = []
        
        for ch , count in freq.items() :
            heap.append((-count, ch))

        heapq.heapify(heap)

        result = []
        prev_ch = ""
        prev_count = 0

        while heap :
            count , ch = heapq.heappop(heap)

            result.append(ch)

            if prev_count < 0 :
                heapq.heappush(heap , (prev_count, prev_ch))
            
            count +=1
            prev_count = count
            prev_ch = ch

        return "".join(result)


