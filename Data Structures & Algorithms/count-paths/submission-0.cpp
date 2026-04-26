class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for(int i = 1;i<m;i++){
            for(int p = 1;p<n;p++){
                dp[i][p] = dp[i-1][p] + dp[i][p-1];
            }
        }
        return dp[m-1][n-1];
    }
};
