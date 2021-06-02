def combinations(arr):
    if len(arr) == 0: return [[]]
    first_element = arr[0]
    rest = arr[1:]

    print('1:', first_element, rest)
    combs_without_first = combinations(rest)
    print(combs_without_first)
    combs_with_first = []

    for i in combs_without_first:
        combs_with_first.append(i)
    combs_with_first.append(first_element)
    print('2:', combs_with_first)


    # combs_without_first.extend(first_element)
    # combs_with_first.append(comb_with_first)
    # print(combs_without_first, comb_with_first, combs_with_first, sep=' # ')

    return combs_with_first


print(combinations(['a', 'b', 'c']))
