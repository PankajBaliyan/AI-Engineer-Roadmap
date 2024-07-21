def Main():
  arr = [12,10,13,5,40]
  # print(bubble_sort(arr))
  print(selection_sort(arr))

# Bubble Sort
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i+1,n):
      if arr[j] < arr[i]:
        arr[i],arr[j] = arr[j],arr[i]
  return arr

# Selection Sort
def selection_sort(arr):
  n = len(arr)