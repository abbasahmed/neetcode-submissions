public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int total = nums.Length;
        int[] result = new int[total * 2];

        for(int i = 0; i<nums.Length; i++){
            result[i] = nums[i];
            result[i+total] = nums[i];
        }
        return result;
    }
}