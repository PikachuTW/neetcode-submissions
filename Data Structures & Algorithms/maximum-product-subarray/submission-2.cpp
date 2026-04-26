class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int dpmin[3000] = {0};
        int dpmax[3000] = {0};

        dpmin[0] = nums[0];
        dpmax[0] = nums[0];

        int ans = nums[0];

        for (int i = 1;i<nums.size();i++){
            for (int j = 0; j < i;j++){
                dpmin[i] = min(dpmin[j] * nums[i], nums[i]);
                dpmin[i] = min(dpmax[j] * nums[i], dpmin[i]);
                dpmax[i] = max(dpmin[j] * nums[i], nums[i]);
                dpmax[i] = max(dpmax[j] * nums[i], dpmax[i]);
            }

            ans = max(ans, dpmax[i]);
        }

        return ans;
    }
};
