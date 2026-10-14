def windowFindMaxDuo(nums: list[int]) -> int:
    sumOfNums = 0

    #92311
    for i in range(len(nums) - 1):
        currentNum = nums[i] + nums[i+1]

        if currentNum > sumOfNums:
            sumOfNums = currentNum


    return sumOfNums