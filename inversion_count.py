def inversion_count(arr):
    length = len(arr)
    if length < 2:
        return arr, 0
    m = length // 2
    left_arr = arr[:m]
    right_arr = arr[m:]
    left_arr, left_inv = inversion_count(left_arr)
    right_arr, right_inv = inversion_count(right_arr)
    result, split_inv = count(left_arr, right_arr)
    return result, left_inv + split_inv + right_inv


def count(l_arr, r_arr):
    length = len(l_arr) + len(r_arr)
    inv = 0
    res = [0] * length
    i = j = 0
    for k in range(length):
        if i == len(l_arr):
            res[k] = r_arr[j]
            j += 1
        elif j == len(r_arr):
            res[k] = l_arr[i]
            i += 1
        elif l_arr[i] <= r_arr[j]:
            res[k] = l_arr[i]
            i += 1
        else:
            res[k] = r_arr[j]
            j += 1
            inv += len(l_arr) - i
    return res, inv


if __name__ == '__main__':
    array = [9, 1, 3, 5, 0, 2, 4, 7, 6]
    array_sort, inversion = inversion_count(array)
    print(inversion, array_sort)
