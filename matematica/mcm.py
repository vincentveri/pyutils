def mcm(numeri):
    mcm = max(numeri)
    while(True):
        result = True
        for x in numeri:
            result = result and (mcm % x == 0)
        if result:
            break
        mcm += 1

    return mcm

if __name__ == "__main__":
    print(mcm([360,240,750]))