# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  if target in arr:
    return arr.index(target)

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  mid = high/2
  while (arr[int(mid)] == arr[int(low)] and arr[int(mid)] != target) or (arr[int(mid)] == arr[int(high)] and arr[int(mid)] != target):
    if arr[int(mid)] == target:
      return arr.index(target)
    elif arr[int(mid)] > target:
      high = mid
      mid = high + low/2
    else:
      low = mid 
      mid = high + mid/2
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  mid = int((low+high)//2)

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[mid] > target:
    binary_search_recursive(arr[low:mid], target, low, mid)
  elif arr[mid] < target:
    binary_search_recursive(arr[mid:high], target, mid, high)
  # if arr[mid] == target:
    return arr.index(target)
