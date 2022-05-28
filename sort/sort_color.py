from typing import List


#  빨간색 0, 흰 색 1, 파란색 2 일 때 순서대로 인접하는 제자리 정렬
#  입력 : [2, 0, 2, 1, 1, 0]
#  출력 : [0, 0, 1, 1, 2, 2]
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

    #  빨간색 0, 흰 색 1, 파란색 2 일 때 순서대로 인접하는 제자리 정렬
    #  입력 : [2, 0, 2, 1, 1, 0]
    #  출력 : [0, 0, 1, 1, 2, 2]
    def selectSortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):           #  [2, 0
            min = i                            #      0, 1]
            for t in range(i + 1, len(nums)):
                if nums[min] > nums[t]:
                    print(f"{min},{t}")
                    print(f"{nums[min]},{nums[t]}")
                    min = t
            if nums[min] != nums[i]:
                nums[min], nums[i] = nums[i], nums[min]



lis = [2, 0, 1]
Solution().selectSortColors(lis)
print(lis)
