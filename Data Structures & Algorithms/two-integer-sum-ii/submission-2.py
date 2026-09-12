class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        second = 1
        for first in range(len(numbers) - 1):
            while second < len(numbers):
                if numbers[first] + numbers[second] == target:
                    return [first + 1, second + 1]
                else:
                    second += 1
            second = first + 2

        