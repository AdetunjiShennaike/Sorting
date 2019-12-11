def partition(data):
    left = []
    pivot = data[0]
    right = []
    for i in data[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return left, [pivot], right
def quicksort(data):
    if len(data) <=1:
        return data
    left, pivot, right = partition(data)
    return quicksort(left)+pivot+quicksort(right)