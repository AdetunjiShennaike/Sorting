# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements):
      if len(arrB) == 0:
        merged_arr[i] = arrA[0]
        del arrA[0]
      elif len(arrA) == 0:
        merged_arr[i] = arrB[0]
        del arrB[0]
      else:
        if arrA[0] < arrB[0]:
          merged_arr[i] = arrA[0]
          del arrA[0]
        elif arrB[0] < arrA[0]:
          merged_arr[i] = arrB[0]
          del arrB[0]
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
      half = int(len(arr)/2)
      arrA = merge_sort(arr[0:half])
      arrB = merge_sort(arr[half:len(arr)])
      return merge(arrA, arrB)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1
    i = 0
    while start <= mid and start2 <= end:
      if arr[start] <= arr[start2]:
        start += 1
      else:
        secondItem = arr[start2]
        index = start2
        
        while index != start:
          arr[index] = arr[index - 1]
          index -= 1
        arr[start] = secondItem 
        start += 1
        mid += 1
        start2 += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l < r:
      half = int(l + (r-l)/2)
      merge_sort_in_place(arr, l, half)
      merge_sort_in_place(arr, half + 1, r)
      return merge_in_place(arr, l, half, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
