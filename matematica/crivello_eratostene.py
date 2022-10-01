def crivello(n):
    intervallo = [x for x in range(2, n)]
    meta = round(len(intervallo) / 2)
    for i in intervallo[:meta]:
        for j in intervallo:
            if j % i == 0 and j > i:
                intervallo.remove(j)
    print(intervallo)


if __name__ == "__main__":
    n = int(input("Inserisci un numero maggiore di 0: "))
    crivello(n)