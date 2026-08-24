class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0 
        p2 = len(nums)

        while p1 < p2:
            if nums[p1] == val:
                p2 -= 1
                nums[p1] = nums[p2]
            else:
                p1 += 1
                
        return p2