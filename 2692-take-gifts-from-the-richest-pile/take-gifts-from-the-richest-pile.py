class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        for i in range(n):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for i in range(k):
            max_val = -heapq.heappop(gifts)
            rem_gifts = math.floor(math.sqrt(max_val))
            heapq.heappush(gifts,-rem_gifts)
        total_rem_gifts = 0
        for i in range(n):
            total_rem_gifts += -gifts[i]
        return total_rem_gifts 
        