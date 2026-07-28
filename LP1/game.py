import pygame, time


pygame.init()

class Janela:
    def __init__(self):

        #Criação do Display
        self.tela =pygame.display.set_mode((300,300))
        self.desenhar()


    def desenhar(self):

        #Loop principal do jogo
        while True:

            #Concertar função de sair
            for evento in pygame.event.get():
                if evento.type== pygame.QUIT:
                    pygame.quit()
                    return
            self.tela.fill(("#2019fb"))
            pygame.display.flip()

# Chamar janela
tela = Janela()