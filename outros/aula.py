import os

pasta = "D:\\Documents\\Codigos\\Atividades\\outros"

for nome_arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    
    # Verifica se é realmente um arquivo (e não uma pasta)
    if os.path.isfile(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(f"--- Conteúdo de {nome_arquivo} ---")
            print(conteudo)
            print()