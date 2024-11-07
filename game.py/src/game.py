import pygame
import random
import os
import sys

pygame.init()

# Configuração da tela
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario Flappy Bird")

# Configuração do relógio
clock = pygame.time.Clock()

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Fontes
font = pygame.font.Font(None, 36)

# Variáveis do jogo
gravity = 0.25
mario_movement = 0
game_active = True
score = 0
speed = 5
level = 1

# Diretório das imagens
current_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(current_dir, 'img')

# Carregando imagens
backgrounds = []
background_files = ['background.png', 'background1.png', 'background2.png', 'background3.png']
for bg_file in background_files:
    full_path = os.path.join(img_dir, bg_file)
    if os.path.exists(full_path):
        bg = pygame.image.load(full_path).convert()
        backgrounds.append(pygame.transform.scale(bg, (width, height)))

mario_surface = pygame.image.load(os.path.join(img_dir, 'mario-yoshi.png')).convert_alpha()
mario_surface = pygame.transform.scale(mario_surface, (50, 50))
mario_rect = mario_surface.get_rect(center=(100, 300))

# Adicionar carregamento da imagem mario-yes.png
mario_yes_surface = pygame.image.load(os.path.join(img_dir, 'mario-yes.png')).convert_alpha()
mario_yes_surface = pygame.transform.scale(mario_yes_surface, (100, 100))

pipe_surface = pygame.image.load(os.path.join(img_dir, 'tubo.png')).convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface, (50, 300))

pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

def create_pipe():
    random_pipe_pos = random.randint(200, 400)
    bottom_pipe = pipe_surface.get_rect(midtop=(800, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(800, random_pipe_pos - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= speed
    return [pipe for pipe in pipes if pipe.right > -50]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def increase_difficulty():
    global speed, level
    speed += 0.1  # Aumento gradual da velocidade
    level = min(level + 1, len(backgrounds))
    spawn_interval = max(1200 - (level * 30), 800)  # Reduz o intervalo de spawn, mas não abaixo de 800ms
    pygame.time.set_timer(SPAWNPIPE, int(spawn_interval))

last_score = 0  # Variável para controlar o último ponto em que a dificuldade aumentou

# Adicionar variável para controlar o estado de vitória
game_won = False

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                mario_movement = -5
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                mario_rect.center = (100, 300)
                mario_movement = 0
                score = 0
                last_score = 0
                speed = 5
                level = 1
                pygame.time.set_timer(SPAWNPIPE, 1200)
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # Desenhar o fundo
    current_background = backgrounds[min(level - 1, len(backgrounds) - 1)]
    screen.blit(current_background, (0, 0))

    if game_active:
        # Movimento do Mario
        mario_movement += gravity
        mario_rect.centery += mario_movement
        screen.blit(mario_surface, mario_rect)

        # Canos
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Colisão
        if mario_rect.top <= -100 or mario_rect.bottom >= 600:
            game_active = False
        for pipe in pipe_list:
            if mario_rect.colliderect(pipe):
                game_active = False

        # Pontuação e dificuldade
        score += 0.01
        current_score = int(score)
        if current_score > last_score and current_score % 10 == 0:
            increase_difficulty()
            last_score = current_score
        
        score_surface = font.render(f'Pontuação: {current_score}', True, black)
        score_rect = score_surface.get_rect(center=(400, 50))
        screen.blit(score_surface, score_rect)

        # Exibir nível atual
        level_surface = font.render(f'Nível: {level}', True, black)
        level_rect = level_surface.get_rect(center=(400, 100))
        screen.blit(level_surface, level_rect)

        # Verificar se o jogador venceu (chegou ao último nível)
        if level > len(backgrounds):
            game_active = False
            game_won = True

    else:
        if game_won:
            # Exibir mensagem de vencedor e imagem mario-yes.png
            winner_surface = font.render('Parabéns! Você venceu!', True, black)
            winner_rect = winner_surface.get_rect(center=(400, 200))
            screen.blit(winner_surface, winner_rect)
            
            mario_yes_rect = mario_yes_surface.get_rect(center=(400, 350))
            screen.blit(mario_yes_surface, mario_yes_rect)
            
            restart_surface = font.render('Pressione ESPAÇO para jogar novamente', True, black)
            restart_rect = restart_surface.get_rect(center=(400, 500))
            screen.blit(restart_surface, restart_rect)
        else:
            game_over_surface = font.render('Pressione ESPAÇO para reiniciar', True, black)
            game_over_rect = game_over_surface.get_rect(center=(400, 300))
            screen.blit(game_over_surface, game_over_rect)

    pygame.display.update()
    clock.tick(60)