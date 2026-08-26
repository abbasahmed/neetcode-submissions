class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        sorted_left = self.sortArray(left)
        sorted_right = self.sortArray(right)
        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right) -> List[int]:
        p1 = 0
        p2 = 0
        result_array = []
        if len(right) == 0:
            return left
        if len(left) == 0:
            return right
        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                result_array.append(left[p1])
                p1 += 1
            elif left[p1] >= right[p2]:
                result_array.append(right[p2])
                p2 += 1
        if p1 == len(left) and p2 != len(right):
            result_array += right[p2:]
        if p2 == len(right) and p1 != len(left):
            result_array += left[p1:]

        return result_array
