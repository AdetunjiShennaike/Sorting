# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    count = cur_index
    smallNum = arr[count]
    while count < len(arr):
      if arr[count] < smallNum:
        smallNum = arr[count]
        smallest_index = count
        count += 1
      else:
        count += 1
    # TO-DO: swap
    temp = arr[cur_index]
    arr[cur_index] = smallNum
    arr[smallest_index] = temp
  return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  swapped = True
  while swapped == True:
    swapped = False
    for i in range(0, len(arr) - 1):
      if arr[i] > arr[i + 1]:
        swapped = True
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr