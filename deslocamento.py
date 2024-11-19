import numpy as np
import matplotlib.pyplot as plt
import json
from progress.bar import Bar

from lib.geral import rho1, rho2, f_nulo, f_constante_factory
from lib.jacobi import calcula_corda as jacobi
from lib.gauss_seidel import calcula_corda as gauss

with open('config.json') as f:
    config = json.load(f)

    config['L'] = float(config['L'])
    config['N'] = int(config['N'])
    config['tolerancia'] = float(config['tolerancia'])
    config['tensao'] = float(config['tensao'])
    config['g'] = float(config['g'])

    config['l0'] = config['L'] / config['N']

def main():
    global config

    print("Tamanho da corda: {}".format(config['L']))
    print("Número de partes: {}".format(config['N']))
    print("Tolerancia: {}".format(config['tolerancia']))
    print("Comprimento das partes: {}".format(config['l0']))
    print("Tensao da corda: {}".format(config['tensao']))
    print("Aceleracao da gravidade: {}".format(config['g']))

    f = f_nulo

    corda0 = jacobi(rho1, f, config)[0]

    deslocamentos = np.zeros(100)
    forcas = np.linspace(0, 10, 100)

    progress = Bar('Calculando deslocamentos', max = 100)
    for i in range(100):
        corda = jacobi(rho1, f_constante_factory(forcas[i], 39), config)[0]
        deslocamentos[i] = corda[39] - corda0[39]
        progress.next()
    progress.finish()

    plt.plot(forcas, deslocamentos)
    plt.show()

main()
