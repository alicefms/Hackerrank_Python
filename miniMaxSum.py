def miniMaxSum(arr):
    soma = 0
    maior = arr[0]
    menor = arr[0]
    for num in arr:
        soma = soma + num
        if (num > maior):
            maior = num
        if num < menor:
            menor = num

    print ((soma - maior) , (soma - menor))

miniMaxSum([1,3,5,7,9])
