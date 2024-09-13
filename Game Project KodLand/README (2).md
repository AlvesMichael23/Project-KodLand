
# Snake Game

Este projeto é um jogo simples da cobrinha (Snake) desenvolvido em Python utilizando a biblioteca pygame. O objetivo é guiar a cobra para comer a comida e ganhar pontos. O jogo termina quando a cobra colide com ela mesma, e você pode reiniciar o jogo pressionando a tecla 'R'.

Requisitos
Antes de rodar o jogo, você deve garantir que tem o pygame instalado. Você pode instalá-lo usando o seguinte comando:

pip install pygame

# Estrutura do Código
Importações e Inicializações:

O código inicia importando as bibliotecas necessárias: pygame, sys, e random.
Inicializa o pygame e configura a música de fundo e os efeitos sonoros.
Configurações do Jogo:

Define as dimensões da tela do jogo e a posição inicial da cobra e da comida.
Inicializa variáveis relacionadas à velocidade, controle e pontuação.
Funções:

aumentaCobra(lista_snake): Desenha a cobra na tela com base na lista de posições.
reiniciar_Jogo(): Reseta o estado do jogo para permitir uma nova partida.
Loop Principal do Jogo:

O loop principal do jogo é responsável por processar eventos, atualizar a posição da cobra, verificar colisões e desenhar elementos na tela.
Inclui o controle dos movimentos da cobra com base nas teclas pressionadas.
Verifica colisões com a comida e com a própria cobra, atualizando a pontuação e a velocidade conforme necessário.
Se a cobra colidir com ela mesma, exibe uma mensagem de "GAME OVER" e aguarda a tecla 'R' para reiniciar o jogo.
Atualização da Tela:

Desenha a cobra, a comida, e a pontuação na tela.
Atualiza a exibição a cada frame com base na taxa de frames definida pelo relógio do jogo.

# Arquivos de Midia

Certifique-se de que os arquivos de mídia necessários estejam no mesmo diretório que o script:

BoxCat Games - Victory.mp3: Música de fundo.
smw_yoshi_runs_away.wav: Efeito sonoro para colisão.

# Instruções para Rodar o Jogo

Execute o script Python:
python nome_do_arquivo.py

Use as teclas de direção para jogar e a tecla 'R' para reiniciar após o término do jogo.

# Problemas e soluções

A cobra não se move: Verifique se a biblioteca pygame está instalada corretamente e se você está utilizando a versão mais recente.

Os arquivos de mídia não são encontrados: Verifique se os arquivos de música e efeitos sonoros estão no diretório correto e com os nomes corretos.