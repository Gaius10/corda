import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

L = 1
N = 10
l0 = L / N
tolerancia = 1e-10
tensao = 2
g = 9.81

def rho1(x):
    return 1

def rho2(x):
    return (1 + np.exp(-100*(x-0.5)**2)) / 2

def calcula_massa(i, rho):
    global l0
    global L

    if i < 0 or i >= N:
        raise Exception("Indice {} inválido (corda dividida em {} partes)".format(i, N))

    if i == 0:
        return integrate.quad(rho, 0, (3/2)*l0)[0]

    if i == N-1:
        return integrate.quad(rho, L - (3/2)*l0, L)[0]

    return integrate.quad(rho, (i+1)*l0 - l0/2, (i+1)*l0 + l0/2)[0]
    # return integrate.quad(rho, i*l0 - l0/2, i*l0 + l0/2)[0]

def calcula_y(i, y, massas):
    global tensao
    global l0
    global g

    if i < 0 or i >= N:
        raise Exception("Indice {} inválido (corda dividida em {} partes)".format(i, N))

    if i == 0 or i == N-1:
        return 0

    y = ( (-l0*massas[i]*g)/(2*tensao) ) + ( (y[i-1] + y[i+1]) / 2 )

    return y

def calcula_corda(rho):
    global N

    massas = np.zeros(N)
    for i in range(N):
        massas[i] = calcula_massa(i, rho)

    y = np.zeros(N)
    novo_y = np.zeros(N)
    iterations = 0
    while True:
        for i in range(1, N-1):
            novo_y[i] = calcula_y(i, y, massas)

        if abs(np.linalg.norm(novo_y - y)) < tolerancia:
            break

        iterations += 1

        y = np.copy(novo_y)

    return y, iterations

def main():
    global l0
    global L
    global N

    print("Tamanho da corda: {}".format(L))
    print("Número de partes: {}".format(N))
    print("Comprimento das partes: {}".format(l0))
    print("Tensao da corda: {}".format(tensao))

    corda, iterations = calcula_corda(rho1)

    print("Iterações: {}".format(iterations))

    x = np.linspace(0, L, N)
    plt.plot(x, corda)
    plt.show()

main()
