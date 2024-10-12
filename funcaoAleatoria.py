import random
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# IMPLEMENTAÇÃO 2° QUESTÃO

limiteSuperior = 999
limiteInferior = -999

def gerar_funcao_primeiro_grau():
    a = random.randint(limiteInferior, limiteSuperior) # Coeficiente para x 
    b = random.randint(limiteInferior, limiteSuperior) # Constante
    
    # Formatar a função de primeiro grau
    funcao = f"{a}*x + {b}"
    return funcao

def gerar_funcao_segundo_grau():
    a = random.randint(limiteInferior, limiteSuperior)  # Coeficiente para x^2
    b = random.randint(limiteInferior, limiteSuperior)  # Coeficiente para x
    c = random.randint(limiteInferior, limiteSuperior)  # Constante
    
    # Formatar a função de segundo grau
    funcao = f"{a}*x**2 + {b}*x + {c}"
    return funcao

def derivada_funcao(funcao_str, valor):
    x = sp.symbols('x')
    # Converte a string da função em uma expressão simbólica
    funcao = sp.sympify(funcao_str)
    # Calcula a derivada da função em relação a x
    derivada = sp.diff(funcao, x)
    # Substitui o valor de x na derivada
    resultado = derivada.subs(x, valor)
    return resultado

def funcao(funcao_str, valor):
    x = sp.symbols('x')
    # Converte a string da função em uma expressão simbólica
    funcao = sp.sympify(funcao_str)
    # Substitui o valor de x na função
    resultado = funcao.subs(x, valor)
    return resultado

def main():
    
    choice = random.randint(1, 2)
    print("Função de " + str(choice) + "° grau")

    if choice == 1:
        func = gerar_funcao_primeiro_grau()
    elif choice == 2:
        func = gerar_funcao_segundo_grau()
    else:
        print("ERRO")
        return
    
    print(f"Função gerada: f(x) = {func}")
    plotar_grafico(func, limiteInferior, limiteSuperior)


# IMPLEMENTAÇÃO 3° QUESTÃO

def plotar_grafico(funcao: str, limiteInferior: float, limiteSuperior: float):
    # Criar um array de valores para x
    x = np.arange(limiteInferior, limiteSuperior, 0.1)

    y = eval(funcao)

    # Valor Inicial
    x0 = (limiteInferior+limiteSuperior)/2
    #Critério de Parada da precisão
    eps1 = 0.1
    eps2 = eps1
    #Critério de Para das Iterações
    maxIteracoes = 20

    # Lista dos valores de x
    listaDeX = [x0]
    iteracao = 0


    plt.figure()
    plt.grid(True)
    plt.plot(x, y,'k')
    plt.xlabel('x')
    plt.ylabel('y', rotation=90)
    plt.title(f'Gráfico da Função Gerada')
    plt.show()




main()
