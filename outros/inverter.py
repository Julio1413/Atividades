palavra = input("Digite uma palavra e descubra se é palíndroma: ")
palavras = palavra[::-1]
if palavra == palavras:print(f"A palavra {palavra} é palíndroma!")
else: print(f"A palavra {palavra} não é palíndroma!")
