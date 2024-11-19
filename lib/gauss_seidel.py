import numpy as np
from lib.geral import calcula_massa


def calcula_y(i, y, novo_y, massas, config):
    tensao = config['tensao']
    l0 = config['l0']
    g = config['g']
    N = config['N']

    if i < 0 or i >= N:
        raise Exception("Indice {} inválido (corda dividida em {} partes)".format(i, N))

    if i == 0 or i == N-1:
        return 0

    y = ( (-l0*massas[i]*g)/(2*tensao) ) + ( (novo_y[i-1] + y[i+1]) / 2 )

    return y

def calcula_corda(rho, config):
    N = config['N']
    tolerancia = config['tolerancia']

    massas = np.zeros(N)
    for i in range(N):
        massas[i] = calcula_massa(i, rho, config)

    y = np.zeros(N)
    novo_y = np.zeros(N)
    iterations = 0

    while True:
        for i in range(1, N-1):
            novo_y[i] = calcula_y(i, y, novo_y, massas, config)

        if abs(np.linalg.norm(novo_y - y)) < tolerancia:
            break

        iterations += 1

        y = np.copy(novo_y)

    return y, iterations