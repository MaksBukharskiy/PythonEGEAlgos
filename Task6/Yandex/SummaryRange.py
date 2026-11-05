def solution_summary(listOfNums: list[int]) -> list[int]:
    l = 0
    r = 0

    result = []

    while l < len(listOfNums):
        while r + 1 < len(listOfNums) and nums[l] + 1 == nums[l+1]:
            r+=1

        if r != l:
            result.append(f'{nums[l]} -> {nums[r]}')

        else:
            result.append(f'{nums[l]}')


        r = l+1
        l = r+1

    return result
