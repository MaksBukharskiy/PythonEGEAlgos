def linearSearch(nums: list[int], target: int) -> int:
    for i, num in enumirate(nums):
        if num == target:
            return i

    return -1