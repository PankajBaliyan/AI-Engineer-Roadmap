def Main():
  # arr = [5,4,1,2,3]
  arr = [1,3,5]
  print(kadane_algorithm(arr))


# def kadane_algorithm(arr):
#     n = len(arr)
#     max_sum = 0
#     for i in range(n):
#         for j in range(i,n):
#             sum = 0
#             for k in range(i,j+1):
#                 sum += arr[k]
#             if sum > max_sum:
#                 max_sum = sum
#     return max_sum

def kadane_algorithm(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

