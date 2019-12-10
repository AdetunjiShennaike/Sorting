# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
  # loop through n-1 elements
  for i in range(0, len(arr) - 1):
    cur_index = i
    smallest_index = cur_index
    # TO-DO: find next smallest element
    # (hint, can do in 3 loc) 
    # Create a count for the select
    count = cur_index
    # define the smallest number as the current number in the array to be check against other numbers
    smallNum = arr[count]
    while count < len(arr):
      # check if a number is smaller if it is then change the smallest number variable and the smallest index count
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
  # Create a check to see if something was swapped
  swapped = True
  # Create a loop that will continue if an item is swapped
  while swapped == True:
    # Start the loop assuming nothing will change
    swapped = False
    for i in range(0, len(arr) - 1):
      # Check if something has to chang if it does change it and switch swapped to true
      if arr[i] > arr[i + 1]:
        swapped = True
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
  # create a holding space for all unique values and a way to count the amount
  holding = []
  holdingCount = []
  for i in range(0, len(arr)):
    # If there is a negative value return an error explaining as such
    if arr[i] < 0: 
      return f"Error, negative numbers not allowed in Count Sort"
    # Check if the current value is already place in the unique values array, if so add 1 if not add it to the array
    if arr[i] in holding:
      index = holding.index(arr[i])
      holdingCount[index] += 1
    else:
      holding.append(arr[i])
      holdingCount.append(1)
  # Empty the arr to begin added the values back in order
  arr = []
  for i in range(0, len(holding)):
    # Create a counter to iterate through, also a small number holder defaulted to the highest value and an index to assure you are using the right count for the held array item
    count = 0
    smallnum = max(holding)
    index = i
    # If the loops finds a smaller value then it replaces the small number holder and the index with the current iteration 
    while count < len(holding):
      if holding[count] <= smallnum and holdingCount[count] > 0:
        smallnum = holding[count]
        index = count
        count += 1
      else: 
        count += 1
    # Using the index, go to the count holder for the smallest value and subtract until you get 0, while adding the smallest value back into the array
    while holdingCount[index] > 0:
      arr.append(smallnum)
      holdingCount[index] -= 1
  return arr