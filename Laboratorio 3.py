import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def crear_arbol_expresiones(expresion):
    # Separar la expresión en operandos y operadores
    operandos = []
    operadores = []
    temp = ""
    for caracter in expresion:
        if caracter in "+-*/":
            operandos.append(temp)
            operadores.append(caracter)
            temp = ""
        else:
            temp += caracter
    operandos.append(temp)

    # Crear un árbol binario a partir de la expresión
    raiz = Nodo(operadores[-1])
    operadores.pop()
    while operandos:
        nodo = Nodo(operandos.pop())
        if not raiz.izquierda:
            raiz.izquierda = nodo
        elif not raiz.derecha:
            raiz.derecha = nodo
        else:
            nodo.derecha = raiz.derecha
            raiz.derecha = nodo
        if operadores:
            raiz.valor = operadores.pop()

    return raiz

def graficar_arbol(nodo, x, y, nivel):
    plt.text(x, y, nodo.valor, fontsize=14, ha='center', va='center')
    if nodo.izquierda:
        plt.plot([x, x - 2 ** (5 - nivel)], [y - 1, y - 2], linewidth=1, color='black')
        graficar_arbol(nodo.izquierda, x - 2 ** (5 - nivel), y - 2, nivel + 1)
    if nodo.derecha:
        plt.plot([x, x + 2 ** (5 - nivel)], [y - 1, y - 2], linewidth=1, color='black')
        graficar_arbol(nodo.derecha, x + 2 ** (5 - nivel), y - 2, nivel + 1)

expresion = "5+((1+2)*4)-3"
arbol = crear_arbol_expresiones(expresion)
graficar_arbol(arbol, 32, 32, 1)
plt.axis('off')
plt.show()
