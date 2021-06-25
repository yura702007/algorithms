def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left_arr, middle_arr, right_arr = [], [], []
    for i in arr:
        if i < pivot:
            left_arr.append(i)
        elif i == pivot:
            middle_arr.append(i)
        else:
            right_arr.append(i)
    return quick_sort(left_arr) + middle_arr + quick_sort(right_arr)


if __name__ == '__main__':
    array = [5, 2, 9]
    print(quick_sort(array))
