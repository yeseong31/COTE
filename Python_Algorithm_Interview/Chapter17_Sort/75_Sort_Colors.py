"""
색 정렬(508p)
빨간색을 0, 흰색을 1, 파란색을 2라 할 때
순서대로 인접하는 제자리 정렬을 수행하라
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
        print(nums)


nums = [2, 0, 2, 1, 1, 0]
sol = Solution()
print(sol.sortColors(nums))
