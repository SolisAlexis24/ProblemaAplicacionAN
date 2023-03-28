from math import exp
import numpy as np
import numdifftools as nd
from scipy.misc import derivative
from tabulate import tabulate
import csv

x0 = 16.5
mr = []
con=1

#se define la funcion
def f(x):
    return (667.38/x)*(1-exp(-(10*x/68.1)))-40

#se representa la fórmula de recurrencia con xn
def recurr(x, cont):
    f1 = nd.Derivative(f)
    xn = x - (f(x)/f1(x))
    #se almacenan las filas de la matriz
    if(x == x0):
        r = [cont-1, x, xn, "-"]
    else:
        r = [cont-1, x, xn, er(xn,x)]
    mr.append(r)
    #se aplica recursividad si el error es mayor a 0.001
    if(er(xn, x) > 0.001):
        cont = cont + 1
        recurr(xn,cont)
    else:
        print("La raiz es: "+str(xn))

#metodo para determinar el error
def er(vr,va):
    return ((abs(vr-va))/vr)*100

#obtencion de la primera y segunda derivada
f0 = f(x0)
f1 = nd.Derivative(f)
ef1 = f1(x0)
f2 = nd.Derivative(f, n=2)
ef2 = f2(x0)

#se obtiene el valor absoluto de G'(x)
critconv = abs((f0*ef2)/ef1**2)

#se aplica el método en caso de cumplir el criterio de convergencia
if(critconv < 1):
    recurr(x0, con)
else:
    print("no cumple criterio de convergencia")
    
#se imprime la tabla con todas las iteraciones realizadas    
print(tabulate(mr,headers=['i','xi',"xi+1","er%"],tablefmt="github"))

