class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = dict()
        ball_map = dict()
        result = list()
        for q in queries:
            ball,color = q
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1
                if(color_map[prev_color] == 0):
                    del color_map[prev_color]
            ball_map[ball] = color
            color_map[color] = color_map.get(color,0)+1 
            result.append(len(color_map))
        return result


            
        