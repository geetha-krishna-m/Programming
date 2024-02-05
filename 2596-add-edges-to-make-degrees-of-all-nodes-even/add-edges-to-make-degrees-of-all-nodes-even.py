class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g={}
        for i in range(len(edges)):
            if edges[i][0] in g:
                g[edges[i][0]].append(edges[i][1])
            else:
                g[edges[i][0]] =[edges[i][1]]
            if edges[i][1] in g:
                g[edges[i][1]].append(edges[i][0])
            else:
                g[edges[i][1]] =[edges[i][0]]
        to_join=[]
        for i in g:
            if len(g[i])%2!=0:
                to_join.append(i)
        print(g,len(g))
        if to_join==[]:
            return True
        if len(to_join)>4 or len(to_join)%2!=0:
            return False
        #print(to_join)
        if len(to_join)==2:
            if to_join[1] not in g[to_join[0]]:
                return True
            else:
                #print("in else")
                for i in g.keys():
                    #print(i,to_join[0],to_join[1])
                    if i==to_join[0] or i==to_join[1]:
                        #print("con")
                        continue
                    #print(to_join[0] not in g[i],to_join[1] not in g[i])
                    if (to_join[0] not in g[i]) and (to_join[1] not in g[i]):
                        return True
                if n>len(g):
                    return True
                return False
                
        if to_join[0] not in g[to_join[1]] and to_join[2] not in g[to_join[3]]:
            return True
        if to_join[0] not in g[to_join[2]] and to_join[1] not in g[to_join[3]]:
            return True
        if to_join[0] not in g[to_join[3]] and to_join[1] not in g[to_join[2]]:
            return True
        
        return False
                
        