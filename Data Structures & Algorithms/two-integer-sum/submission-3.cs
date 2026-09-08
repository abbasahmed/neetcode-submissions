public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> hashmap = new Dictionary<int, int>();
        for(int i=0; i < nums.Length; i++){
            var diff = target - nums[i];
            if (hashmap.ContainsKey(diff)){
                return new int[] {hashmap[diff], i};
            }
            hashmap[nums[i]] = i;
        }
        return null;
    }
}
