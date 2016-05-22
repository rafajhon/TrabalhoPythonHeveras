def media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)
if __name__ == "__main__":
    lista=list()
    while (1):
        entrada = int(input("entre com um numero da lista ou 0 para finalizar"+
                            " lista: "))
        if entrada == 0:
            break
        lista.append(entrada)
    teste = media(lista)
    print("Media da lista de numeros: ", teste)
