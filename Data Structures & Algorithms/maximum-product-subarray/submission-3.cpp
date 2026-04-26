class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int dpmin[30000] = {0};
        int dpmax[30000] = {0};

        dpmin[0] = nums[0];
        dpmax[0] = nums[0];

        int ans = nums[0];

        for (int i = 1;i<nums.size();i++){
                dpmin[i] = min(dpmin[i-1] * nums[i], nums[i]);
                dpmin[i] = min(dpmax[i-1] * nums[i], dpmin[i]);
                dpmax[i] = max(dpmin[i-1] * nums[i], nums[i]);
                dpmax[i] = max(dpmax[i-1] * nums[i], dpmax[i]);

            ans = max(ans, dpmax[i]);
        }

        return ans;
    }
};
