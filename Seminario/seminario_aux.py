import random
from itertools import permutations

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
    for i in range(len(l)):
        expr += str(l[i])
        if i < len(l) - 1:
            expr += O[i]
    return expr

def space(n):
    return list(permutations(range(1,n+1),5))

def fuerza_bruta(val):
    pos = space(9) # posibles soluciones para 1..9 numeros
    print(pos)
    for p in pos:
        expr = calcular(p)
        print(eval(expr))
        if eval(expr) == val:
            return expr
    return len(pos)


if __name__ == "__main__":
    print(fuerza_bruta(4))