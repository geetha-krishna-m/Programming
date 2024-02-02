class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        n = len(roads)
        maxy = 1000001
        d,path = dict(),dict()
        for i in range(n):
            d[(roads[i][0],roads[i][1])] = roads[i][2]
            d[(roads[i][1],roads[i][0])] = roads[i][2]
            if roads[i][0] in path:
                path[roads[i][0]].append(roads[i][1])
            if roads[i][1] in path:
                path[roads[i][1]].append(roads[i][0])
            if roads[i][0] not in path:
                path[roads[i][0]] = [roads[i][1]]
            if roads[i][1] not in path:
                path[roads[i][1]] = [roads[i][0]]
        queue = [1]
        visited = set()
        miny = 1000001
        while queue:
            front = queue.pop(0)
            visited.add(front)
            for i in path[front]:
                if i not in visited:
                    queue.append(i)
                    miny = d[(front,i)] if d[(front,i)] < miny else miny
        return miny
                
            