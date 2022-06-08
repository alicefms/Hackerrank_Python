def plusMinus(arr):
    positivos = 0
    negativos = 0
    zeros = 0
    for e in arr:
        if e==0:
            zeros = zeros +1
        elif e>0:
            positivos= positivos +1
        elif e<0:
            negativos= negativos +1
    print('{0:7.6}'.format(positivos/len(arr)))
    print('{0:7.6}'.format(negativos/len(arr)))
    print('{0:7.6}'.format(zeros/len(arr)))

plusMinus([1,1,0,-1,-1])