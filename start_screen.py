import pygame

def start_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    largura = 570
    altura = 600
    window = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Speed Menzinho')  
    # Carrega o fundo da tela inicial
    background = pygame.image.load('sprites/TELAS/tela inicial.png').convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(30)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = 0
                running = False

            if event.type == pygame.KEYUP:
                state = 1
                running = False

        # A cada loop, redesenha o fundo e os sprites
        window.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


