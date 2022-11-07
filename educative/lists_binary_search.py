"""
implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

Input#
A list and a number k

Output#
A list with two integers a and b that add up to k
"""
from typing import List


def binary_search(lst, k):
    first = 0
    last = len(lst) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == k:
            found = True
            index = mid
        else:
            if lst[mid] < k:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum(lst, k):
    lst.sort()
    for i in range(len(lst)):
        index = binary_search(lst, k - lst[i])
        if index != -1 and index != i:
            return [lst[i], k - lst[i]]


# print(find_sum([1, 5, 3], 2))
# print(find_sum([1, 2, 3, 4], 5))


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        found = False
        index = -1
        while first <= last and not found:
            mid = (first + last) // 2
            print(first, last, mid, nums[mid])
            if nums[mid] == target:
                found = True
                index = mid
                break
            else:
                if nums[mid] > target:
                    last = mid - 1
                else:
                    first = mid + 1
        if found:
            return index
        else:
            return -1

print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))
