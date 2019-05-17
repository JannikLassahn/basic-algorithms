def bubblesort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(0, i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

# quicksort


def quicksort(l):
    if len(l) <= 1:
        return l

    smaller = []
    larger = []
    equal = []
    pivot = l[0]

    for x in l:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)


def quicksort_inplace(l, start, end):
    if start >= end:
        return

    i = start - 1
    pivot = l[end]

    for j in range(start, end):
        if l[j] <= pivot:
            i = i + 1
            l[i], l[j] = l[j], l[i]

    l[i + 1], l[end] = l[end], l[i + 1]
    pivot = i + 1

    quicksort(l, start, pivot - 1)
    quicksort(l, pivot + 1, end)

# mergesort


def mergesort(l):
    if len(l) <= 1:
        return l

    pivot = len(l) // 2

    left = mergesort(l[:pivot])
    right = mergesort(l[pivot:])

    result = []
    leftIndex, rightIndex = 0, 0
    for _ in range(0, len(l)):
        if leftIndex == len(left):
            result.extend(right[rightIndex:])
            break
        elif rightIndex == len(right):
            result.extend(left[leftIndex:])
            break
        elif right[rightIndex] < left[leftIndex]:
            result.append(right[rightIndex])
            rightIndex += 1
        else:
            result.append(left[leftIndex])
            leftIndex += 1

    return result

