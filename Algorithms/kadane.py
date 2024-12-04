def kadane(arr):
    start, end = 0, 0
    temp_start = 0
    max_sum = 0
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i

        if current_sum < 0:
            temp_start = i + 1
            current_sum = 0

    return start, end


kadane(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
kadane(arr=[-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4])
