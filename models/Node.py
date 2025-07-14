
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
        
        
def criar_lista_encadeada(valores):
    if not valores:
        return None
    cabeca = Node(valores[0])
    atual = cabeca
    for valor in valores[1:]:
        atual.proximo = Node(valor)
        atual = atual.proximo
    return cabeca


def imprimir_lista_encadeada(cabeca):
    atual = cabeca
    ultimo_valor = None
    while atual:
        if atual.valor != ultimo_valor:
            print(atual.valor)
            ultimo_valor = atual.valor
        atual = atual.proximo

