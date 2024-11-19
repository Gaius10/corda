import numpy as np
import scipy.integrate as integrate

def rho1(x):
    return 1

def rho2(x):
    return (1 + np.exp(-100*(x-0.5)**2)) / 2

def calcula_massa(i, rho, config):
    L = config['L']
    l0 = config['l0']
    N = config['N']

    if i < 0 or i >= N:
        raise Exception("Indice {} inválido (corda dividida em {} partes)".format(i, N))

    if i == 0:
        return integrate.quad(rho, 0, (3/2)*l0)[0]

    if i == N-1:
        return integrate.quad(rho, L - (3/2)*l0, L)[0]

    return integrate.quad(rho, (i+1)*l0 - l0/2, (i+1)*l0 + l0/2)[0]

def f(i):
    return 0
