
def all_construct(target, words, memo={}):
    if target in memo: return memo[target]
    if target == '': return [[]]

    result = []
    for word in words:
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            # print(word, ':', target, '->', suffix)
            suffix_ways = all_construct(suffix, words, memo)
            if len(suffix_ways):
                target_ways = list(map(lambda x: [word, *x], suffix_ways))
                # print(target, '>', target_ways, '>>', suffix_ways)
                result.extend(target_ways)
    memo[target] = result
    return result


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # 1
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) # 2
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # 0
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(all_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
  'e',
  'ee',
  'eee',
  'eeee',
  'eeeee',
  'eeeeee'
])) # 0
