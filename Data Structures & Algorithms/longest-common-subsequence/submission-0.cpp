class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int dp[1000][1000] = {0};
        dp[0][0] = (1 ? text1[0] == text2[0]: 0);
        for(int p = 1;p<text2.size();p++){
            if (text1[0] == text2[p] || dp[0][p-1] == 1){
                dp[0][p] = 1;
            }
        }
        for(int p = 1;p<text1.size();p++){
            if (text2[0] == text1[p] || dp[p-1][0] == 1){
                dp[p][0] = 1;
            }
        }
        for(int i = 1;i<text1.size();i++){
            for(int p =1;p<text2.size();p++){
                dp[i][p] = max(dp[i-1][p], dp[i][p]);
                dp[i][p] = max(dp[i][p-1], dp[i][p]);
                if (text1[i] == text2[p])dp[i][p] = max(dp[i-1][p-1]+1,dp[i][p]);
            }
        }
        return dp[text1.size()-1][text2.size()-1];
    }
};
