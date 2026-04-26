class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[100000] = {0};
        for (int i = 1; i<=amount; i++){
            int k = INT_MAX;
            for(int& coin: coins){
                if (i >= coin && dp[i-coin] != INT_MAX){
                    k = min(k, dp[i-coin] + 1);
                }
            }
            dp[i] = k;
        }

        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
