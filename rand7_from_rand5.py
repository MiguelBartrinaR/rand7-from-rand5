import random

def rand5():
    # Función random de un entero entre 1 y 5
    return random.randint(1, 5)

def rand7():
    while True:
        num = (rand5() - 1) * 5 + rand5() # Numero uniforme entre 1 y 25
        if num <= 21: # Descartar valores entre 22-25 y repetir
            return (num - 1) % 7 + 1 # uniforme entre 1 y 7

def main():
    # Generar 10 números aleatorios entre 1 y 7
    for i in range(10):
        print(rand7())

if __name__ == "__main__":
    main()
