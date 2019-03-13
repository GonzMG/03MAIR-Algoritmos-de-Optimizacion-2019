import random

N = ["1","2","3","4","5","6","7","8","9"]
O = ["+","-","*","/"]

class Nodo:
    def __init__(self, nums, padre):
        self.nums = nums
        self.cost = self.cost()
        self.padre = padre


def algoritmo_a(val):
    a = eval(N[0])
    print(a)
    return a

def calcular(l):
    expr = ""
    for i in l:
        expr += i
        if i != len(l):
            expr += O[i]
    return expr

def fbruta(val):
    pass

if __name__ == "__main__":
    target = 4
    sol = algoritmo_a(target)