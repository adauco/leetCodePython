from typing import List


def getConcatenation(self, nums: List[int]) -> List[int]:
    conta = nums + nums
    return conta


def buildArray(self, nums: List[int]) -> List[int]:
    # for x in nums:  print(x)
    return [nums[i] for i in nums]


if __name__ == '__main__':
    print(getConcatenation('', 'Juan '))
    cars = ["Ford", "Volvo", "BMW"]
    buildArray('', cars)
