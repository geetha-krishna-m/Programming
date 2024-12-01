class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        freq = dict()
        for ind,val in enumerate(arr):
            freq[val] = ind
        for ind,i in enumerate(arr):
            if i*2 in freq and freq[i*2]!=ind:
                return True
        return False