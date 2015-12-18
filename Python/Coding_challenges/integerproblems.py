#problems for number lists and integer challenges

"""You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products."""
def multi_allnums(lst):
    while len(lst) > 1:
        lst[0] *= lst[1]
        del lst[1]
    return lst[0]

def multi_list(lst):
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    return prod
#returns product of all integers except at its on index
def get_products_of_all_ints_except_at_index(lst):
    prods = []
    for elem in lst:
        copy = lst[:]
        copy.remove(elem)
        prods.append(multi_list(copy))
    return prods