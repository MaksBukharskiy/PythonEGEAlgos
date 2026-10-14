def move_zeroes(nums: list[int]) -> list[int]:
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]

            nums[i] = nums[position]
            nums[position] = temp
            
            position+=1
            #012303

    return nums
