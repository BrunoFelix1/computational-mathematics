import random

# IMPLEMENTAÇÃO 2° QUESTÃO

# Faixa de valores possíveis para os coeficientes (única parte pseudo-random)
limiteSuperior = 99
limiteInferior = -99

def gerar_funcao_constante():
    a = random.randint(limiteInferior, limiteSuperior)
    return f"{a}"

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

def gerar_funcao_aleatoria():
    # Se for escolhido 1 - Função de primeiro grau; se for 2 - De Segundo Grau; se for 3 - Constante
    
    tipo_funcao = random.choice([1, 2, 3])

    if tipo_funcao == 1:
        print("Função de " + str(tipo_funcao) + "° grau")
        func = gerar_funcao_primeiro_grau()
    elif tipo_funcao == 2:
        print("Função de " + str(tipo_funcao) + "° grau")
        func = gerar_funcao_segundo_grau()
    elif tipo_funcao == 3:
        print("Função constante")
        func = gerar_funcao_constante()
    else:
        print("ERRO")
        return
    print(f"Função gerada: f(x) = {func}")
    return func
