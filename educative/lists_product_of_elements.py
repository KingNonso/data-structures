"""
initialize an array to be returned arr =
loop through the list and
multiply all the elements except the current element being looped over
"""
# def find_product(lst):
#     # Write your code here
#     products = []
#     left = 1
#     for i in range(len(lst)):
#         ans = 1
#         for j in lst[i+1:]:
#             print(ans, i, j, products)
#             ans *= j
#         products.append(ans*left)
#         left *= lst[i]
#     return products

def find_product(lst):
    # get the product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left *= ele
        print('left', left, product)
    # print('product', product, left)
    # get the product start from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        print('right', right, product, i)
        right = right * lst[i]

    return product

print(find_product([1, 2, 3, 4]))
# print(find_product([0, 2, 9, 0, 12, 25]))
