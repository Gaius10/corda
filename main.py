import numpy as np
import matplotlib.pyplot as plt
import json

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

    # f = f_nulo

    f1 = f_constante_factory(2, 17)
    f2 = f_constante_factory(-2, 30)
    f = lambda i: f1(i) + f2(i)

    corda_jacobi, iterations_jacobi = jacobi(rho1, f, config)
    print("Iterações pelo método de Jacobi: {}".format(iterations_jacobi))

    corda_gauss, iterations_gauss = gauss(rho1, f, config)
    print("Iterações pelo método de Gauss-Seidel: {}".format(iterations_gauss))

    x = np.linspace(0, config['L'], config['N'])
    plt.plot(x, corda_jacobi, linestyle="solid", color="green", label="Jacobi", marker="o", markersize=2)
    plt.plot(x, corda_gauss, linestyle='dotted', color="red", label="Gauss-Seidel", marker="o", markersize=2)
    plt.legend()
    plt.show()

main()
