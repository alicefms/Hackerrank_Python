def lonelyinteger(a):
    a.sort()
    for indice in range(0, (len(a)),2):
        if indice == (len(a)-1):
            print('aqui')
            return a[indice]
        elif a[indice] == a[indice +1]:
            continue
        else:
            return a[indice]


print(lonelyinteger([1,2,3,4,3,2,1]))