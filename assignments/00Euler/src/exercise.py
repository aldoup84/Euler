
import os

# Imprime valores tabulares del Método de Euler
def printTablaEuler(x,y):
    print(f"{'x':>8}{'y':>8}")
    print(f"{'----------------':16}")
    for i in range(0,len(x)):
        print(f"{x[i]:8.2f}{y[i]:8.2f}")

# Método de Euler
def Euler(f,x,y, ls, h):
    i=1
    while i * h <= ls:
        x = x + [(x[i-1]+h)]
        y = y + [(y[i-1] + f(x[i-1],y[i-1])*h)]

        i=i+1
    
    return x,y

def main():
    #escribe tu código abajo de esta línea

    os.system("clear")
    print("METODO DE EULER-CAUCHY")

    # Ecuacion Diferencial
    f = lambda x,y : -2 * x ** 3 + 12 * x ** 2 - 20 * x + 8.5

    # Condiciones iniciales
    x=[0]
    y=[1]

    ls=4
    h=0.5

    # Resolviendo la Eucacion Diferencial por el Método de Euler
    x,y = Euler(f,x,y,ls,h)

    # Mostrando la solución tabular
    printTablaEuler(x,y)

if __name__=='__main__':
    main()
