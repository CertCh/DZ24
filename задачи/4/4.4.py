def longest_nonincreasing_subsequence(arr):
    if not arr:
        return []

    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] >= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_length = max(dp)
    subsequence = []
    for i in range(len(arr) - 1, -1, -1):
        if dp[i] == max_length:
            subsequence.append(arr[i])
            max_length -= 1
    
    return subsequence[::-1]

arr = [5, 3, 4, 8, 6, 7]
print(longest_nonincreasing_subsequence(arr))
