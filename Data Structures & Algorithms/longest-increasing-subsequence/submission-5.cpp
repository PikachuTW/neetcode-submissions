class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int dp[2000] = {0};
        dp[0] = 1;
        int ans = 1;
        for (int i = 1;i<nums.size();i++){
            int mm = 0;
            for (int p = 0;p<i;p++){
                if (dp[p] > mm && nums[p] < nums[i]){
                    mm = max(mm, dp[p]);
                }
            }
            dp[i] = mm + 1;
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};
