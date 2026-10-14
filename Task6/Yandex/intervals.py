def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]:
    sorted_intervals = intervals.sort(key= lambda k:k[0])
    merged = []

    for interval in sorted_intervals:
        if len(merged == 0) or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            

    return merged

