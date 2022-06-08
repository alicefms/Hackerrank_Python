def minimumBribes(q):
    def func (q):
        troca = 0
        esperado =[]
        for i in range(len(q)):
            esperado.append(i+1)
        for n in range(len(q)):
            if q[n] != esperado[n]:

                if q[n] == esperado[n+1]:
                    esperado[n], esperado[n+1] = esperado[n+1], esperado[n]
                    troca = troca + 1

                elif q[n] == esperado[n+2]:
                    esperado[n], esperado[n + 1], esperado[n + 2] = esperado[n + 2], esperado[n], esperado[n +1]
                    troca = troca + 2

                else:
                    return 'Too chaotic'
                    break
        return(troca)

    print(func(q))

minimumBribes([1,2,3,5,4,6,7,8])  #1
minimumBribes([4,1,2,3]) #Too chaotic
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) #too chaotic
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) #7
minimumBribes([2,1,5,3,4]) #3
minimumBribes([3,1,2]) #2