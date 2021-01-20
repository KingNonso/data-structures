# the grid traveler problem in python

def grid_traveler(m, n, memo = {}):
    key = str(m) + ','+str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1;
    if m == 0 or n == 0: return 0;
    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    # print(memo)
    return memo[key]

print(grid_traveler(2, 3))
print(grid_traveler(4, 5))
print(grid_traveler(6, 7))
print(grid_traveler(18, 18))


