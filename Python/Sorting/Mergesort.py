#file implementaiton for merge sort

#checks if an integer is still in the list
def isseparated(lst):
    return isinstance(lst, int)


def divide_lists(lst):
    if isseparated(lst):
        return lst
    else:
        return divide_lists(lst[:len(lst)//2])

def mergeSort(lst):
    if len(lst)>1:
        mergeSort(lst[:len(lst)//2])
        mergeSort(lst[len(lst)//2:])
        i, j, k = 0, 0, 0
        lefthalf = lst[:len(lst)//2]
        righthalf = lst[len(lst)//2:]
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
        return lst


