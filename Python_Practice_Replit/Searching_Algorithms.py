def Main():
  arr = [5, 2, 4, 7, 1, 3, 2, 6]
  print(linear_search(arr, 40))
  arr = [1, 2, 18, 23, 55, 66, 70]
  print(binary_search(arr, 2))


def linear_search(arr, target):
  n = len(arr)
  for i in range(n):
    if arr[i] == target:
      return i
  return -1


def binary_search(arr, target):
  n = len(arr)
  low, high = 0, n - 1
  while (low <= high):
    mid = (low + high) // 2
    if (arr[mid] == target):
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1
