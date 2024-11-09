def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def kth_smallest_sort(arr, k):
    # Sort the array using insertion sort
    insertion_sort(arr)
    # Return the k-th smallest element (0-based index)
    return arr[k - 1]