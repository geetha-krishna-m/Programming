class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks,n = 0,len(arr)
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            if(curr_sum == ((i)*(i+1)//2)):
                chunks += 1
        return chunks
