def search_template(string, template):
    N = len(template)
    M = len(string)
    if M < N:
        return

    def offsets():
        end_symbol = template[-1]
        offsets_dict = {}
        for k, s in enumerate(template[N - 2::-1]):
            if s not in offsets_dict:
                offsets_dict[s] = k + 1
            else:
                continue
        if end_symbol not in offsets_dict:
            offsets_dict[end_symbol] = N
        offsets_dict['*'] = N
        return offsets_dict

    table_offsets = offsets()
    j, i = N - 1, N - 1
    while j < M:
        if string[j] == template[i]:
            j -= 1
            i -= 1
            if i == 0:
                return j
        elif string[j] not in table_offsets:
            j += table_offsets['*']
            i = N - 1
        else:
            j += table_offsets[string[j]]
            i = N - 1


if __name__ == '__main__':
    result = search_template('лилилилась', 'лилила')
    print(result)
