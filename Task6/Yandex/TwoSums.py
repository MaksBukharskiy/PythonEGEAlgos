def SolutionOf_TwoSums(listOfNums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerated(listOfNums):
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[i] = num

        
        