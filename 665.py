from typing import List



def checkPossibility(nums: List[int]) -> bool:
    deleted = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            deleted += 1
    return deleted <= 1

print(checkPossibility([4, 2, 1]))