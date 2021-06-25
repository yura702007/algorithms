def search_in_string(string, template):
    n, m = len(string), len(template)
    if n < m:
        return

    def max_prefix():
        prefixes = [0] * m
        d, k = 0, 1
        while k < m:
            if template[k] == template[d]:
                prefixes[k] = d + 1
                d += 1
                k += 1
            elif d == 0:
                k += 1
            else:
                d -= 1
        return prefixes

    prefix_list = max_prefix()
    j, i = 0, 0
    while j < n:
        if string[j] == template[i]:
            j += 1
            i += 1
            if i == m:
                return j - m
        elif i == 0:
            j += 1
        else:
            i = prefix_list[i - 1]


if __name__ == '__main__':
    print(search_in_string('лилилось лилилась', 'илила'))
