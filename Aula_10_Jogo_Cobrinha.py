import pygame
import time
import random

pygame.init()

branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

largura_tela = 800
altura_tela = 600

tamanho_bloco = 10
velocidade = 15

fonte = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')


def pontuacao(pontos):
    valor = fonte_pontuacao.render("Sua Pontuação: " + str(pontos), True, preto)
    tela.blit(valor, [0, 0])

def nossa_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def mensagem(msg, cor):
    mesg = fonte.render(msg, True, cor)
    tela.blit(mesg, [largura_tela / 6, altura_tela / 3])


def jogo():
    fim_jogo = False
    game_over = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_mudanca = 0
    y1_mudanca = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0

    while not fim_jogo:

        while game_over == True:
            tela.fill(branco)
            mensagem("Você perdeu! Pressione C-Continuar ou Q-Sair", vermelho)
            pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_over = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, preto, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_over = True

        nossa_cobra(tamanho_bloco, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        clock = pygame.time.Clock()
        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()

