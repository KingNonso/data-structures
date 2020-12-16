def can_construct(target, words, memo={}):
    if target in memo: return memo[target]
    if target == '': return True

    for word in words:
        # print(word)
        if word in target and target.index(word) == 0:
            suffix = target[len(word):]
            memo[target] = can_construct(suffix, words)
            if memo[target] is True:
                return True

    return False



print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # true
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # false
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # true
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
  'e',
  'ee',
  'eee',
  'eeee',
  'eeeee',
  'eeeeee'
])) # false



