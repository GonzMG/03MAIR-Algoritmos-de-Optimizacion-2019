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


if __name__ == "__main__":
    a = [45,12,36,85,95,45,1,56]
    d = bubblesort_stop(a, len(a))
    print(d)
