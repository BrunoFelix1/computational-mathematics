from ui import tela
from botoes import switch_case
equacao = []
resultado = A = B = C = D = E = F = X = Y = M = None
num_decimais = 2
shift = alpha = store = False

while True:
    tela(equacao, resultado)
    entrada = input("Escolha um botão: ")
    equacao, resultado, shift, alpha, store, num_decimais, A, B, C, D, E, F, X, Y, M = switch_case(equacao, resultado, entrada, shift, alpha, store, num_decimais, A, B, C, D, E, F, X, Y, M)