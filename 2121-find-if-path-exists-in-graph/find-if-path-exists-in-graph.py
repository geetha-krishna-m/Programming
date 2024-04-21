# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         d = dict()
#         for i in edges:
#             if i[0] in d and i[1] not in d[i[0]]:
#                 d[i[0]].append(i[1])
#             if i[1] in d and i[0] not in d[i[1]]:
#                 d[i[1]].append(i[0])
#             if i[0] not in d:
#                 d[i[0]] = [i[1]]
#             if i[1] not in d:
#                 d[i[1]] = d[i[0]]
#         if source == destination:
#             return True
#         res = [source]
#         visited = set()
#         while len(res)>0:
#             node = res.pop(0)
#             visited.add(node)
#             for i in d[node]:
#                 if i not in visited:
#                     res.append(i)
#                 if i == destination:
#                     return True              
#         return False
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        if source == destination:
            return True
        
        queue = deque([source])
        visited = set([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
