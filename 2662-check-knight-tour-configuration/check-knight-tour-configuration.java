class Solution {
    int[][] directions = new int[][]{{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}};
    public boolean checkValidGrid(int[][] grid) {
        
        int n = grid.length;
        boolean[][] visited = new boolean[n][n];
        visited[0][0] = true;
        return backtrack(grid, visited, 0, 0, 1);
    }
    private boolean backtrack(int[][] grid, boolean[][] visited, int row, int col, int count) {
        int n = grid.length;
        if (count == n * n) {
            return true;
        }

        for (int[] dir : directions) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && !visited[newRow][newCol] && grid[newRow][newCol] == count) {
                visited[newRow][newCol] = true;
                if (backtrack(grid, visited, newRow, newCol, count + 1)) {
                    return true;
                }
                visited[newRow][newCol] = false;
            }
        }

        return false;
    }

}