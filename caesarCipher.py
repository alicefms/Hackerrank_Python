def caesarCipher(s, k):
#97 a 122 /// 65 a 90
#num=ord(char)
#char=chr(num)

    nova_s = ''
    for letra in s:
        if ord(letra) in range(65, 91) or ord(letra) in range(97, 123):
            if letra.isupper():
                letra = chr(ord(letra) + k)
                while (ord(letra)>90):
                    letra = chr(ord(letra) -26)
            if letra.islower():
                letra = chr(ord(letra) + k)
                while (ord(letra)>122):
                    letra = chr(ord(letra) -26)
        nova_s = nova_s + letra
    return nova_s

print(caesarCipher('Alice', 2))