class Solution {
public:
    bool canJump(vector<int>& nums) {
        int power = nums[0];
        for(int i = 1;i<nums.size();i++){
            power --;
            if (power < 0)return false;
            power = max(power, nums[i]);
        }
        return true;
    }
};
