def fibonacci(fibb):
    if fibb < 2:
        return fibb
    f = fibonacci(fibb-1) + fibonacci(fibb-2)
    return f
if __name__ == "__main__":
    fibb = int(input("entre com um numero"));
    print('fibonacci (%d) =  %d'%(fibb,fibonacci(fibb)))
