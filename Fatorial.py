def fatorial(numero):
    if numero:
        return numero * fatorial(numero - 1)
    return 1
if __name__ == "__main__":
    numero =int(input(" Entre com numero:  "))
    print("Fatorial(%d) = %d "%(numero,fatorial(numero))) 
