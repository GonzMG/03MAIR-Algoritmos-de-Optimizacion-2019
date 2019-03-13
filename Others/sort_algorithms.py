import numpy as np

def bubblesort_stop(l, x):
    swap_flag = 0
    for i in range(1,x):
        if l[i-1] > l[i]:
            l[i-1], l[i] = l[i], l[i-1]
            swap_flag = 1
    if swap_flag == 1:
        return bubblesort_stop(l,x-1)
    else:
        return l

def bubblesort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

#Pivot: last element
def quicksort_gonz(l):
    if(len(l) <= 1): #end of recursivity
        return l
    else:
        p = l[len(l)-1] # pivot element
        s = -1 # position of the lowest element
        for i in range(len(l)):
            if l[i] <= p:
                s+=1
                l[s], l[i] = l[i], l[s]
            if(i == len(l) - 1): #end of the list
                return quicksort_gonz(l[:s]) + [l[s]] + quicksort_gonz(l[s+1:])


def quicksort_unai(a):
    if len(a)<=1:
        return a
    if len(a)==2:
        return [min(a),max(a)]
    pivot = np.random.choice(a)
    less = []
    greater = []
    equal = []
    for i in a:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)
    return quicksort_unai(less) + equal + quicksort_unai(greater)


if __name__ == "__main__":
    a = [45,12,36,85,95,45,1,56]
    # b = bubblesort_stop(a.copy(), len(a))
    # c = bubblesort(a.copy())
    d = quicksort_gonz(a)
    print(d)
