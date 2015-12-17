#file that implements that quicksort

#creates a random list of integers between 1 and 30 of length n
def random_intlist(n):
    import random
    return [random.randrange(1, 30) for i in range(n)]

#swaps places for two indexes in a list
def swapitems(lst, i, j):
    holder = lst[i]
    lst[i] = lst[j]
    lst[j] = holder
#returns index of random pivot
def select_pivot(lst):
    import random
    return random.randrange(len(lst)//2, len(lst)-1)
#bool for ordering with pivot
def less_than(lst, begin, pivot):
    return lst[begin] < lst[pivot]

def issorted(lst):
    return lst == sorted(lst)
#takes a value at position i in a list, pops it, and inserts it behind position j
def rotate_val(lst, i, j):
    lst.insert(j+1, lst.pop(i))

#implements quicksort recursively
def quicksort(lst):
    if issorted(lst):
        return lst
    else:
        pivot = select_pivot(lst)
        piv_val = lst[pivot]
        i = 0
        while i < pivot:
            if not less_than(lst, i, pivot):
                rotate_val(lst, i, pivot)
                i += 1
            else:
                i += 1
        return quicksort(lst)
#single run of quicksort
def sing_quicksort(lst):
    pivot = select_pivot(lst)
    piv_val = lst[pivot]
    i = 0
    while i < pivot:
        if not less_than(lst, i, pivot):
            rotate_val(lst, i, pivot)
            i += 1
        else:
            i += 1
    return quicksort(lst)


