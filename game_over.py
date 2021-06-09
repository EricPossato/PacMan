import pygame

def game_over(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    largura = 570
    altura = 600
    window = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Speed Menzinho')  
    # Carrega o fundo da tela inicial
    background = pygame.image.load('sprites/TELAS/tela final.png').convert()
    background_rect = background.get_rect()
    pygame.mixer.music.load('sprites/sons/FINAL.mp3')
    pygame.mixer.music.set_volume(0.1)

    pygame.mixer.music.play(loops=-1)
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
                if event.key == pygame.K_RETURN:
                    state = 2
                    running = False
                    pygame.mixer.music.stop()

        # A cada loop, redesenha o fundo e os sprites
        window.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


