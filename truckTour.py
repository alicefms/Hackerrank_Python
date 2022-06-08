def truckTour (arr):
    def teste(indice, arr):
        reserva = arr[indice][0]
        for e in range(indice, len(arr)):
            gas = arr[e][0]
            dist = arr[e][1]

            if reserva>dist:
                reserva = reserva - dist + gas
                print reserva
                continue
            else:
                return 0
        return 1

    for e in arr:
        gasolina =e[0]
        distancia = e[1]
        if gasolina> distancia:
            if teste(arr.index(e), arr) == 1:
                return arr.index(e)
            else:
                continue


#teste
#print(truckTour([[1, 5], [10, 3], [3, 4]]))
print(truckTour([[3, 4], [4, 1], [4, 4]]))