def array_challenge(arr):
    seats = arr[0]
    filled = arr[1:]
    answer = 0

    for i in range(1, seats):
        if i not in filled:
            answer += check_available(i, filled, seats)
    return answer

def check_available(i, filled, seats):
    answer = 0
    if i % 2 == 0:
        even_space = i + 2
        if even_space not in filled and even_space <= seats:
            answer += 1
    elif i % 2 == 1:  # this means it is odd
        first_space = i + 1
        if first_space not in filled and first_space <= seats:
            answer += 1
        second_space = i + 2
        if second_space not in filled and second_space <= seats:
            answer += 1
    return answer


print(array_challenge([8, 1, 8]))
print(array_challenge([6, 4]))
print(array_challenge([12, 2, 6, 7, 11]))
