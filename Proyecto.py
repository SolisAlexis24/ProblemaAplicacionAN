from math import exp, log
from scipy.misc import derivative
import numpy as np
from tabulate import tabulate
import csv
c0 = 16.5 #Valor semilla proporcionado por el problema
mr = []

def G1(c):
    #Despeje 1 de la funcion original
    return -6.81*log(1-(0.06*c))

def G2(c):
    #Despeje 2 de la funcion original
    return 16.6848*(1-exp(-10*c/68.1))

def ccAS(G):
    dc1 = derivative(G,c0,dx=1e-6) #Se deriva y evalua la funcion
    if(abs(dc1)<1):
        return True
    else:
        return False

def consTable(G):
    if(ccAS(G)):
        x=CalcR(G,c0,15,-1)
        print(tabulate(mr,headers=['i','xi',"xi+1","er%"],tablefmt="github"))
        print("La raiz es: ",x)
        guardarTabla()
    else:
        print("Este despeje NO cumple el criterio y por lo tanto no se puede seguir")

def CalcR(G, xi, xj,i): ##Funcion para calcular la raiz
    if(er(xj, xi) > 0.001):
        i=i+1
        xj = G(xi)
        f = [i, xi, xj, er(xj, xi)]
        mr.append(f)
        return CalcR(G, xj, xi,i)  # llamada recursiva
    else:
        return xi # caso base

def er(vr,va):
    return ((abs(vr-va))/vr)*100

def guardarTabla():
    with open('data.csv', mode='w', newline='') as arch:
        writer = csv.writer(arch, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'xi', 'xi+1', 'er%'])  # escribir la primera fila con los nombres de las columnas
        for fila in mr:
            writer.writerow(fila)  # escribir cada fila de la matriz en el archivo CSV

consTable(G2)