
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
        
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None  # Mantém o último nó para inserção rápida

    def adicionar(self, valor):
        novo = Node(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            self.cauda.proximo = novo
            self.cauda = novo
            
    def __iter__(self):
        atual = self.cabeca
        while atual:
            yield atual.valor
            atual = atual.proximo

def criar_lista_encadeada(valores):
    if not valores:
        return None
    cabeca = Node(valores[0])
    atual = cabeca
    for valor in valores[1:]:
        atual.proximo = Node(valor)
        atual = atual.proximo
    return cabeca


