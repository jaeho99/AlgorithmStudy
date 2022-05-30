#  정렬된 배열을 받아 덧셈을하여 타겟을 반들 수 있는 배열의 두 숫자 인덱스를 리턴하라
#  주의: 이문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.
#  numbers = [2, 7, 11, 15], target = 9
#  [1, 2]
from typing import List


def twoSum(nums: List[int], target: [int]) -> List[int]:
    left, right = 0, len(nums)-1
    while left != right:
        if nums[right] + nums[left] < target:
            left += 1
        elif nums[right] + nums[left] > target:
            right -= 1
        else:
            return left + 1, right + 1

# 지은님 코드 문제 확인--------------------
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         def binary_search(numbers, target):
#             left = 0
#             right = len(numbers) - 1
#             print(f"돌고돌아 target{target}")
#             while left <= right:
#
#                 mid = (left + right) // 2
#                 print(f"left: {left} right: {right} mid : {mid}")
#                 # 겹쳐지는 숫자가 나오는 경우 -> mid를 오늘쪽으로 한 칸 이동
#                 if numbers[mid] == target:
#                     return mid
#                 elif numbers[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return None
#
#         for i, n in enumerate(numbers):
#             t = target - n
#             result = binary_search(numbers, t)
#             if result:                           #  수정
#                 return [i+1, result+1]
#             else:
#                 continue

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         def binary_search(numbers, target, idx):
#             left = 0
#             right = len(numbers) - 1
#             print(f"돌고돌아 target{target}")
#             while left <= right:
#
#                 mid = left + (right - left) // 2  # 수정
#                 print(f"left: {left} right: {right} mid : {mid}")
#                 # 겹쳐지는 숫자가 나오는 경우 -> mid를 오늘쪽으로 한 칸 이동
#                 if numbers[mid] > target:  # 수정
#                     right = mid - 1
#                 elif numbers[mid] < target:
#                     left = mid + 1
#                 else:
#                     return mid
#             return None
#
#         for i, n in enumerate(numbers):
#             t = target - n
#             result = binary_search(numbers, t, i)
#             if result:  # 수정
#                 return [i + 1, result + 1]
#             else:
#                 continue
#         지은님 코드 끝 ----------------

# 선용님코드

# import bisect
# import collections
# from typing import List
#
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         dict = collections.defaultdict(int)
#         ## 딕셔너리를 value와 key+1값으로 만든다
#         for i in range(len(numbers)):
#             dict[numbers[i]]=i
#
#         ## 리스트를 돌며 [target-요소값]인 값이 딕셔너리에 있는지 확인한다
#         for idx in range(len(numbers)):
#             if dict[target-numbers[idx]]:
#                 return sorted([idx+1,dict[target-numbers[idx]]+1])
#
# sol = Solution()
# # print(sol.twoSum([2,7,11,15],9))
# # print(sol.twoSum([2,3,4],6))
# # print(sol.twoSum([-1,0],-1))
# print(sol.twoSum([1,2,3,4,4,9,56,90],8))
# numbers = [1, 2, 3, 4, 4, 9, 56, 90]
#
# print(twoSum(numbers, 8))
