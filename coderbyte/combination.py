def combinations(arr):
    if len(arr) == 0: return [[]]
    first_element = arr[0]
    rest = arr[1:]

    combs_without_first = combinations(rest)
    combs_with_first = []

    for x in combs_without_first:
        comb_with_first = [*x, first_element]
        combs_with_first.append(comb_with_first)
        print(x, comb_with_first, combs_with_first, sep=' # ')

    return [*combs_with_first, *combs_without_first]


print(combinations(['a', 'b', 'c']))
