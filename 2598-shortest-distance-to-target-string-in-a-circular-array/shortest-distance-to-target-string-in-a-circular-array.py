class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        w = len(words)
        for i in range(w-1):
            if(words[(startIndex-i+w)%w] == target):
                return i
            if(words[(startIndex+i)%w] == target):
                return i
        return -1
            
        