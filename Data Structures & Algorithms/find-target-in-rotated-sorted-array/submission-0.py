class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left half sorted 
                if nums[left] <= target < nums[mid]:
                    # target in left half
                    right = mid - 1
                else:
                    # target in right half
                    left = mid + 1
            else:
                # right half sorted
                if nums[mid] < target <= nums[right]:
                    # target in right half
                    left = mid + 1
                else:
                    # target in left half
                    right = mid - 1

        return -1