class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int [][][] magicSquares = {
            {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}},
            {{2, 7, 6}, {9, 5, 1}, {4, 3, 8}},
            {{6, 1, 8}, {7, 5, 3}, {2, 9, 4}},
            {{8, 3, 4}, {1, 5, 9}, {6, 7, 2}},
            {{4, 3, 8}, {9, 5, 1}, {2, 7, 6}},
            {{2, 9, 4}, {7, 5, 3}, {6, 1, 8}},
            {{6, 7, 2}, {1, 5, 9}, {8, 3, 4}},
            {{8, 1, 6}, {3, 5, 7}, {4, 9, 2}}
        };
        int row = grid.length,col = grid[0].length;
        int cnt = 0;
        if(row<3 || col<3){
            return cnt;
        }
        for(int i=0;i<=row-3;i++){
            for(int j=0;j<=col-3;j++){
                int[][] subgrid = new int[3][3];
                for(int si=0;si<3;si++){
                    for(int sj=0;sj<3;sj++){
                        subgrid[si][sj] = grid[i+si][j+sj];
                    }
                }
                for(int mi=0;mi<=7;mi++){
                    if(Arrays.deepEquals(subgrid,magicSquares[mi])){
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
}