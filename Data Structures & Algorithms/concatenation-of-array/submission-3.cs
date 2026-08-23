public class Solution {
    public int[] GetConcatenation(int[] nums) {
        // int total = nums.Length;
        int[] result = new int[nums.Length * 2];

        // for(int i = 0; i<nums.Length; i++){
        //     result[i] = nums[i];
        //     result[i+total] = nums[i];
        // }

        Array.Copy(nums, 0, result, 0, nums.Length);
        Array.Copy(nums, 0, result, nums.Length, nums.Length);
        return result;
    }
}