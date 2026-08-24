public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int p1 = 0;
        int p2 = nums.Length;

        while (p1 < p2){
            if (nums[p1] == val){
                p2 = p2 - 1;
                nums[p1] = nums[p2];
            }
            else {
                p1 = p1 + 1;
            }
        }
        return p2;
    }
}