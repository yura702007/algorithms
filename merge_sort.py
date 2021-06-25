def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    m = length // 2
    left, right = arr[:m], arr[m:]
    left, right = merge_sort(left), merge_sort(right)
    return merge(left, right)


def merge(arr_1, arr_2):
    length = len(arr_1) + len(arr_2)
    res = [0] * length
    j, i = 0, 0
    for k in range(length):
        if j == len(arr_1):
            res[k] = arr_2[i]
            i += 1
        elif i == len(arr_2):
            res[k] = arr_1[j]
            j += 1
        elif arr_1[j] <= arr_2[i]:
            res[k] = arr_1[j]
            j += 1
        else:
            res[k] = arr_2[i]
            i += 1
    return res


if __name__ == '__main__':
    not_sort_list = [25, 6, -87, 3, 0, 9, 54, 6, 8, 7, 0, -1, 56, 42, -12]
    sort_list = merge_sort(not_sort_list)
    print(sort_list)
