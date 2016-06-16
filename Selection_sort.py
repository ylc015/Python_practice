import sys

def selectionSort(a):

    for i in range(len(a)):

        smallest = sys.maxsize

        smallest_index = 0

        for j in range(i,  len(a)):

            if a[j] < smallest:

                smallest = a[j]

                smallest_index = j


        swap(a, i , smallest_index)

    return a

def swap(a , i , j):

    if not a: return

    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

tests = []
tests.append([3, 4,5 ,2, 4, 5, 2,3,4, 3, 5])
tests.append([1,1,1,1,1,1])
tests.append([])

for test in tests:
    assert selectionSort(test) == sorted(test)
