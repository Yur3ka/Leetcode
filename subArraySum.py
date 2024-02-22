def subArraySum(arr, n, s):
    # Write your code here
    sum = 0
    start = 0
    for i in range(n):
        sum += arr[i]
        if sum == s:
            return [start + 1, i + 1]
        elif sum < s:
            continue
        else:
            sum -= arr[start]
            start += 1
            if sum == s:
                return [start + 1, i + 1]
    return [-1]


print(subArraySum([1, 2, 4, 5, 6, 3, 4, 2, 7, 8, 9], 11, 45))
print(subArraySum([1, 2, 3, 7, 5], 5, 12))
