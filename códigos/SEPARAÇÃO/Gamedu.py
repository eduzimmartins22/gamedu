import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("FORCA CME")
icone = pygame.image.load("img_9.png")
pygame.display.set_icon(icone)
fim_de_jogo = False
linhas = 2
colunas = 13
espacamento = 20
tamanho = 40
caixas = []

for linha in range(linhas):
    for coluna in range(colunas):
        x = ((coluna * espacamento) + espacamento) + (tamanho * coluna)
        y = ((linha * espacamento) + espacamento) + (tamanho * linha) + 330
        caixa = pygame.Rect(x, y, tamanho, tamanho)
        caixas.append(caixa)

botoes = []
A = 65

for ind, caixa in enumerate(caixas):
    letra = chr(A + ind)
    botao = [caixa, letra]
    botoes.append(botao)

def desenhar_botoes(botoes):
    for caixa, letra in botoes:
        texto_botao = fonte.render(letra, True, (0, 0, 0))
        retangulo_botao = texto_botao.get_rect(center=(caixa.x + 20, caixa.y + 20))
        tela.blit(texto_botao, retangulo_botao)
        pygame.draw.rect(tela, (0, 0, 0), caixa, 2)

def exibir_palavra():
    texto_display = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            texto_display += f"{letra}"
        else:
            texto_display += '_'
    texto = fonte_letra.render(texto_display, True, (0, 0, 0))
    tela.blit(texto, (400, 200))

imagens = []
hangman_status = 0

palavras = ['EDUGAME', 'PYTHON', 'JAVA', 'OLÁ', 'PALAVRA', 'FORCA', 'TEMPO', 'LEÃO', 'RANDOM']
palavra = random.choice(palavras)
letras_adivinhadas = []

imagem = pygame.image.load("imagem_banner_contato.jpg")
imagens.append(imagem)

fonte = pygame.font.SysFont("arial", 30)
fonte_jogo = pygame.font.SysFont("arial", 80)
fonte_letra = pygame.font.SysFont("arial", 60)

titulo = "GAMEDU"
texto_titulo = fonte_jogo.render(titulo, True, (0, 0, 0))
retangulo_titulo = texto_titulo.get_rect(center=(largura // 2, texto_titulo.get_height() // 2 + 10))

executando = True
while executando:
    tela.fill((255, 255, 255))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicao_clique = evento.pos

            for botao, letra in botoes:
                if botao.collidepoint(posicao_clique):
                    if letra not in palavra:
                        hangman_status += 1
                    if hangman_status == 6:
                        fim_de_jogo = True
                    letras_adivinhadas.append(letra)
                    botoes.remove([botao, letra])

                    for i in range(5):
                        if hangman_status == 1:
                            imagem = pygame.image.load("cabeça.png")
                            imagens.append(imagem)
                            print("A cabeça já foi adicionada.")
                        elif hangman_status == 2:
                            imagem = pygame.image.load("peitoral.png")
                            imagens.append(imagem)
                            print("Peitoral adicionado.")
                        elif hangman_status == 3:
                            imagem = pygame.image.load("braços.png")
                            imagens.append(imagem)
                            print("Os dois braços também foram adicionados.")
                        elif hangman_status == 4:
                            imagem = pygame.image.load("pernas.png")
                            imagens.append(imagem)
                            print("Pernas adicionadas.")
                        elif hangman_status == 5:
                            imagem = pygame.image.load("pes.png")
                            imagens.append(imagem)
                            print("Pés adicionados.")
                        elif hangman_status == 6:
                            imagem = pygame.image.load("game_over.png")
                            imagens.append(imagem)
                            executando = False

            tela.blit(imagem, (150, 150))
            for caixa in caixas:
                pygame.draw.rect(tela, (0, 0, 0), caixa, 2)
                ganhou = True
                for letra in palavra:
                    if letra not in letras_adivinhadas:
                        ganhou = False
                if ganhou:
                    fim_de_jogo = True
                    texto_jogo = "VOCÊ GANHOU, PARABÉNS!!!"
                else:
                    texto_jogo = "TE FATIEI INTEIRO ANTES, VOCÊ PERDEU"

                desenhar_botoes(botoes)
                exibir_palavra()
                tela.blit(texto_titulo, retangulo_titulo)
                clock.tick(50)
                pygame.display.update()

                if fim_de_jogo:
                    tela.fill((255, 255, 255))
                texto = fonte_jogo.render(texto_jogo, True, (0, 0, 0))
                retangulo_texto = texto.get_rect(center=(largura // 2, altura // 2))
                tela.blit(texto, retangulo_texto)
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
                pygame.quit()
