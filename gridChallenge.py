def gridChallenge(grid):
    n = len(grid[0])
    new_grid = []

    for s in grid:
        lista = list(s)
        lista.sort()
        new_grid.append(lista)
    for i in range(n):
        teste = []
        teste2 = []
        for word in new_grid:
            teste.append(word[i])
        for letra in teste:
            teste2.append(letra)
        teste2.sort()
        if teste != teste2:
            return 'NO'
    return 'YES'
#teste
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])) #YES
print(gridChallenge(['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv'])) #YES