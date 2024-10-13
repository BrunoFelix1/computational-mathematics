import random
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import math

# IMPLEMENTAÇÃO 2° QUESTÃO

limiteSuperior = 99
limiteInferior = -99

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

def derivada_funcao_resultado(funcao_str, valor):
    x = sp.symbols('x')
    # Converte a string da função em uma expressão simbólica
    funcao = sp.sympify(funcao_str)
    # Calcula a derivada da função em relação a x
    derivada = sp.diff(funcao, x)
    # Substitui o valor de x na derivada
    resultado = derivada.subs(x, valor)
    return resultado


def funcao_resultado(funcao_str, valor):
    x = sp.symbols('x')
    funcao = sp.sympify(funcao_str)  
    # Verifica se valor é um único número ou uma lista/array
    if isinstance(valor, (list, np.ndarray)):
        resultado = [funcao.subs(x, v) for v in valor]  # Aplica a função para cada valor de x
    else:
        resultado = funcao.subs(x, valor)  # Aplica a função para um único valor de x
    return resultado

# Gera uma função aleatória de primeiro ou segundo grau e plota o gráfico dela
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

    plt.figure()
    plt.grid()
    plt.plot(x,funcao_resultado(funcao,x), 'k-')
    # Valor Inicial
    x0 = 12
    # Critério de Parada da precisão
    eps1 = 0.1
    eps2 = eps1
    # Critério de Para das Iterações
    maxIteracoes = 20
    # Lista dos valores de x
    listaDeX = [x0]
    iteracao = 0
    # Critério de parada: precisão + iterações
    while ((math.fabs(funcao_resultado(funcao,x0)) > eps1) & (iteracao <= maxIteracoes)):
        print('[',x0,']')
        #Calculando o próximo x
        xk = float(x0 - (funcao_resultado(funcao,x0)/derivada_funcao_resultado(funcao,x0)))
        listaDeX.append(xk)
        if (math.fabs(funcao_resultado(funcao, x0)) < eps1)|((math.fabs(xk-x0)) < eps2):
            break
        else:
            x0 = xk
        iteracao = iteracao + 1

    #Esse é o cont para os índices dos x
    cont = 0
    for x in listaDeX:
        plt.plot(x,funcao_resultado(funcao, x),'ro')
        nome = '$x_'+str(cont)+'$'
        plt.text(x, 0.1, nome, fontsize=10)
        plt.xlabel('x')
        plt.ylabel('y', rotation=180)
        plt.title(f'Gráfico da Função Gerada')
        cont = cont + 1
    print('[',xk,']')
    print('Número de iterações:', iteracao+1)
    print('Precisão |f(xk)|:',math.fabs(funcao_resultado(funcao, xk)))
    print('Precisão |xk-x0|:',math.fabs(xk-x0))
    plt.show()




main()
