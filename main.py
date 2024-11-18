import numpy as np
import scipy.integrate as integrate

L = 1
N = 10
l0 = L / N
tolerancia = 1e-6
tensao = 2
g = 9.81

def rho1(x):
    return 1

def rho2(x):
    return (1 + np.exp(-100*(x-0.5)**2)) / 2

def massa(i, rho):
    global l0
    global L

    if i < 0 or i >= N:
        raise Exception("Indice inválido (corda dividida em {} partes)".format(N))

    if i == 0:
        return integrate.quad(rho, 0, (3*l0)/2)[0]

    if i == N-1:
        return integrate.quad(rho, L - (3*l0)/2, L)[0]

    return integrate.quad(rho, (i+1)*l0 - l0/2, (i+1)*l0 + l0/2)[0]

def y(i, rho):
    global tensao
    global l0
    global g

    if (i < 0 or i >= N):
        raise Exception("Indice inválido (corda dividida em {} partes)".format(N))

    if i == 0 or i == N-1:
        return 0

    A = np.array([ tensao / l0, -2 * tensao / l0, tensao / l0 ])
    b = np.array([ massa(i, rho) * g ])

    x = jacobi(A, b)
    return x[1]

def jacobi(A, b):
    global tolerancia
    x = np.zeros(len(A))
    iterations = 0

    while True:
        iterations += 1
        D = np.diag(A) * np.identity(len(A))
        R = A - D
        next_x = (b - R@x) / np.diag(A)

        if abs(np.linalg.norm(next_x - x) < tolerancia):
            break

        x = next_x

    return x

def main():
    global l0
    print("Tamanho da corda: {}".format(L))
    print("Número de partes: {}".format(N))
    print("Comprimento das partes: {}".format(l0))
    print("Tensao da corda: {}".format(tensao))

    for i in range(N):
        print("y({}) = {}".format(i, y(i, rho1)))


main()
