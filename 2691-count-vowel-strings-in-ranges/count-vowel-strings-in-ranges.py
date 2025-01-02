class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hash_map = dict()
        n,cnt = len(words),0
        def check(chars):
            if(chars == 'a' or chars=='e' or chars == 'i' or chars == 'o' or chars == 'u'):
                return True
            return False
        for i in range(n):
            if(check(words[i][0]) and check(words[i][-1])):
                cnt = cnt + 1
            hash_map[i] = cnt
        q = len(queries)
        res = []
        for i in range(q):
            sums = hash_map[queries[i][1]] - (hash_map[queries[i][0]-1] if(queries[i][0]>0) else 0)
            res.append(sums)
        return res