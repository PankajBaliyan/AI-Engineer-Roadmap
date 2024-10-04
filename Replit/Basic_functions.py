def Main():
  arr = [5, 2, 4, 7, 1, 3, 2, 6]
  print("Original array:", arr)

  arr.insert(2, 10)
  print("Array after inserting 10 at index 2:", arr)

  arr.append(5)
  print("Array after appending 5:", arr)

  arr.remove(5)
  print("Array after removing 5:", arr)

  arr.pop()
  print("Array after popping:", arr)

  arr[0] = 10
  print("Array after updating index 0:", arr)
