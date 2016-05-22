def soma_fib(fibb):
    if fibb < 2:
        return fibb
    f = soma_fib(fibb-1) + soma_fib(fibb-2)
    return f
if __name__ == "__main__":
    fibb = int(input("entre com um numero"));
    print('fibbonaci (%d) =  %d'%(fibb,soma_fib(fibb)))
