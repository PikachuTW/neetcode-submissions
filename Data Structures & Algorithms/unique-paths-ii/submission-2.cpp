class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n));
        dp[0][0] = 1 - obstacleGrid[0][0];
        for(int i = 0;i<m;i++){
            for(int p = 0;p<n;p++){
                if (obstacleGrid[i][p] == 1){
                    dp[i][p] = 0;
                    continue;
                }
                if (i > 0){
                    dp[i][p] += dp[i-1][p];
                }
                if (p > 0){
                    dp[i][p] += dp[i][p-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
};


