
def best_sum(target, arr, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    # print(target, memo)

    last = None
    for i in arr:
        remainder = target - i
        remainder_result = best_sum(remainder, arr, memo)
        if remainder_result is not None:
            result = [*remainder_result, i]
            if last is None or len(result) < len(last):
                last = result

    memo[target] = last
    return last

# print(best_sum(7, [2,3]))
# print(best_sum(7, [5,3,4,7]))
print(best_sum(7, [2,4]))
# print(best_sum(8, [2,3,5]))
# print(best_sum(100, [1,2,5,25]))


