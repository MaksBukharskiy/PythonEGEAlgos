def best_time(nums: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for number in nums:
        if number < min_price:
            min_price = number

        else:
            current_profit = number - min_price

            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit
