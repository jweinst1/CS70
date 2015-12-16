#code for implementing bubble sort in python

#creates a random list of integers between 1 and 30 of length n
def random_intlist(n):
    import random
    return [random.randrange(1, 30) for i in range(n)]

#swaps places for two indexes in a list
def swapitems(lst, i, j):
    holder = lst[i]
    lst[i] = lst[j]
    lst[j] = holder

def isless(a, b):
    return a < b

#multi-run bubble sort
def bubblesort(lst):
    i = 0
    while lst != sorted(lst):
        if i == len(lst)-1:
            i = 0 #new run through the list
        elif lst[i] > lst[i+1]:
            swapitems(lst, i, i+1)
            i += 1
        else:
            i += 1
    return lst
#one bubble search run
def singlebubrun(lst):
    i = 0
    while i < len(lst)-1:
        if lst[i] > lst[i+1]:
            swapitems(lst, i, i+1)
            i += 1
        else:
            i += 1
    return lst
#counts the number of times until a list is bubble sorted
def countbubbleruns(lst):
    if lst == sorted(lst):
        return 0
    else:
        i = 0
        while lst != sorted(lst):
            lst = singlebubrun(lst)
            i += 1
        return i


