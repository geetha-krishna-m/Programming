class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = dict()
        # for i in strs:
        #     res = []
        #     for j in i:
        #         res.append(j)
        #     ans = "".join(sorted(res))
        #     if ans in d:
        #         d[ans].append(i)
        #     else:
        #         d[ans] = [i]
        # return list(d.values())
        d = dict()
        for i in strs:
            res = str(sorted(i))
            if res not in d:
                d[res] = [i]
            else:
                d[res].append(i)
        return d.values()