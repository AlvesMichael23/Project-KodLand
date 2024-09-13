#Inicialização da biblioteca pygame
import pygame 
from pygame.locals import*
from sys import exit 
from random import randint

pygame.init()

#Musica de fundo
musica_fundo = pygame.mixer.music.load('BoxCat Games - Victory.mp3')
pygame.mixer.music.play(-1)


barulho_colisao = pygame.mixer.Sound('smw_yoshi_runs_away.wav')


#Definição do tamanho da tela do jogo
larguraTela = 1080
alturaTela = 720

#Valor que a cobra surge na tela
X_snake = int(larguraTela/2)
Y_snake = int(alturaTela/2)

#Valores de espaço que a comida da cobra vai randomizar dentro da tela
x_food = randint(35, 700)
y_food = randint(50, 300)

velocidade = 10
x_controle = 20
y_controle = 0


pontos = 0
fonte = pygame.font.SysFont('arial', 25, True, False)



tela = pygame.display.set_mode((larguraTela, alturaTela ))
pygame.display.set_caption('Snake Game')  
relogio = pygame.time.Clock()
lista_snake = []
comprimeto_inicial = 5
morreu = False

def aumentaCobra(lista_snake):
    for XeY in lista_snake:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 15, 15))

def reiniciar_Jogo():
    global pontos, comprimeto_inicial, X_snake, Y_snake, lista_snake, lista_tamanho, x_food, y_food, morreu
    pontos = 0
    comprimeto_inicial = 5
    X_snake = int(larguraTela/2)
    Y_snake = int(alturaTela/2)
    lista_snake = []
    lista_tamanho = []
    x_food = randint(35, 700)
    y_food = randint(50, 300)
    morreu = False


while True:
    
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    formatoTexto = fonte.render(mensagem, False, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade       
    
    X_snake = X_snake + x_controle
    Y_snake = Y_snake + y_controle

    snake = pygame.draw.rect(tela, (0, 255, 0), (X_snake, Y_snake, 15, 15))
    food = pygame.draw.rect(tela, (255,0,0), (x_food,y_food,15,15))
    
    if snake.colliderect(food):
        x_food = randint(35, 700)
        y_food = randint(50, 300)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimeto_inicial = comprimeto_inicial + 1

    lista_tamanho = []    
    lista_tamanho.append(X_snake)
    lista_tamanho.append(Y_snake)

    
    lista_snake.append(lista_tamanho)
    
    if lista_snake.count(lista_tamanho) > 1:
        fonte2 = pygame.font.SysFont('arial', 40, True, True)
        mensagem = 'GAME OVER!: Press R'
        texto = fonte2.render(mensagem, True, (0,0,0))
        

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_Jogo()        
            
            tela.blit(texto, (larguraTela//2, alturaTela//2))
            pygame.display.update() 
              
    
    if X_snake > larguraTela:
        x_controle = 0
    if X_snake < 0:
        X_snake = larguraTela
    if Y_snake < 0:
        Y_snake = alturaTela
    if Y_snake > alturaTela:
        Y_snake = 0



    if len(lista_snake) > comprimeto_inicial:
        del lista_snake[0]

    aumentaCobra(lista_snake)

    tela.blit(formatoTexto, (920, 0))
    pygame.display.update()        