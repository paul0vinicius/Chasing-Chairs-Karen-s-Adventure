# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame

from pygame.locals import *

# Game specification:
GAME_SCREEN = pygame.display.set_mode((800, 650))
TITLE = "Chasing Chairs: Karen's Adventure"
ICON = 'karen/characther.png'

# Game colors:
YELLOW = (255,255,0)
WHITE = (255, 255, 255)

# Character movement:
KAREN = 'karen/characther.png'
KAREN_BACK = 'karen/karen_costas.png'
KAREN_UP1 = 'karen/karen_cima1.png'
KAREN_UP2 = 'karen/karen_cima2.png'
KAREN_DOWN1 = 'karen/c_down.png'
KAREN_DOWN2 = 'karen/c_down2.png'
KAREN_LEFT = 'karen/karen_esquerda.png'
KAREN_LEFT1 = 'karen/karen_esquerda1.png'
KAREN_LEFT2 = 'karen/karen_esquerda2.png'
KAREN_RIGHT = 'karen/karen_direita.png'
KAREN_RIGHT1 = 'karen/karen_direita1.png'
KAREN_RIGHT2 = 'karen/karen_direita2.png'
KAREN_DANCING1 = 'karen/danca/danca1.png'
KAREN_DANCING2 = 'karen/danca/danca3.png'
KAREN_DANCING3 = 'karen/danca/danca4.png'
FROZEN_KAREN = 'karen/karen_congelada.png'
KAREN_WINS = 'karen/karen_wins.png'
KAREN_FLAG = 'images/karen_wins.png'
KAREN_KEYBOARD = 'images/teclas_karen.png'
KAREN_SIT = 'karen/karen_sentada.png'

# Player 2 movement:
PLAYER2 = 'player2/player2.png'
PLAYER2_BACK = 'player2/player2_costas.png'
PLAYER2_UP1 = 'player2/player2_cima1.png'
PLAYER2_UP2 = 'player2/player2_cima2.png'
PLAYER2_DOWN1 = 'player2/player2_down.png'
PLAYER2_DOWN2 = 'player2/player2_down2.png'
PLAYER2_LEFT = 'player2/player2_esquerda.png'
PLAYER2_LEFT1 = 'player2/player2_esquerda1.png'
PLAYER2_LEFT2 = 'player2/player2_esquerda2.png'
PLAYER2_RIGHT = 'player2/player2_direita.png'
PLAYER2_RIGHT1 = 'player2/player2_direita1.png'
PLAYER2_RIGHT2 = 'player2/player2_direita2.png'
PLAYER2_DANCING1 = 'player2/danca/danca7.png'
PLAYER2_DANCING2 = 'player2/danca/danca8.png'
PLAYER2_DANCING3 = 'player2/danca/danca9.png'
FROZEN_PLAYER2 = 'player2/player2_congelada.png'
PLAYER2_WINS = 'player2/player2_wins.png'
PLAYER2_FLAG = 'images/player2_wins.png'
PLAYER2_KEYBOARD = 'images/teclas_inimiga.png'
PLAYER2_SIT = 'player2/player2_sentada.png'

# Players' life:
P2_3LIFES = 'player2/player23vidas.png'
P2_2LIFES = 'player2/player22vidas.png'
P2_1LIFE = 'player2/player21vida.png'
K_3LIFES = 'karen/karen3vidas.png'
K_2LIFES = 'karen/karen2vidas.png'
K_1LIFE = 'karen/karen1vida.png'

# Wins:
ONE_VICTORY = 'images/1vitoria.png'
TWO_VICTORIES = 'images/2vitorias.png'
THREE_VICTORIES = 'images/3vitorias.png'
FOUR_VICTORIES = 'images/4vitorias.png'
FIVE_VICTORIES = 'images/5vitorias.png'
SIX_VICTORIES = 'images/6vitorias.png'
SEVEN_VICTORIES = 'images/7vitorias.png'
EIGHT_VICTORIES = 'images/8vitorias.png'
NINE_VICTORIES = 'images/9vitorias.png'
TEN_VICTORIES = 'images/10vitorias.png'

# Sound effects:
SHOW_CHAIR = 'sounds/cadeira_aparece.wav'
PLAYER_GETS_BONUS = 'sounds/pega_poder.wav'
BONUS_OVER = 'sounds/acaba_poder.wav'
ICE_BONUS = 'sounds/bonus_gelo.wav'
SHOES_BONUS = 'sounds/bonus_sapatinho.wav'
RESET_BONUS_SOUND = 'sounds/yahoo.wav'
GAME_OVER = 'sounds/game_over.wav'

# Power ups:
SKATE = 'images/speed_bonus.png'
ICE = 'images/cristal_gelo.png'
RESET_BONUS = 'images/reset_bonus.png'

# Wall:
WALL = 'images/parede.png'

# Musics:
MENU_MUSIC = 'music/come_and_getit_full.mp3'
FINAL_MUSIC = 'music/girl_gone_wild.mp3'

PLAYLIST = ['music/bad_girls.mp3','music/anaconda.mp3','music/problem.mp3','music/she_wolf.mp3',
            'music/diva_que_vc_quercopiar.mp3', 'music/applause.mp3', 'music/pumpit.mp3', 'music/wakemeup.mp3',
            'music/come_and_getit.mp3', 'music/i_loveit.mp3', 'music/nao_olha_pro_lado.mp3', 'music/where_them_girlsat.mp3',
            'music/starships.mp3', 'music/where_have_u_been.mp3', 'music/turn_me_on.mp3', 'music/dark_cavalinho.mp3',
            'music/who_run_the_world.mp3', 'music/only_girl.mp3', 'music/hotncold.mp3', 'music/ET.mp3', 'music/primadonna.mp3',
            'music/yala.mp3','music/work.mp3', 'music/scream_and_shout.mp3', 'music/tik_tok.mp3', 'music/lalala.mp3',
            'music/beijinho_no_ombro.mp3', 'music/rude_boy.mp3', 'music/lalala.mp3', 'music/radioactive.mp3', 'music/good_feeling.mp3',
            'music/toxic.mp3', 'music/on_the_floor.mp3', 'music/i_need_ur_love.mp3', 'music/bubble_double.mp3', 'music/break_free.mp3',
]

# Backgrounds:
BACKGROUND_MENU = 'backgrounds/back_menu.jpg'
FINAL_BACKGROUND = 'backgrounds/final_background.jpg'
LEVEL1 = 'backgrounds/level1.jpg'
LEVEL2 = 'backgrounds/level2.jpg'
LEVEL3 = 'backgrounds/level3.jpg'
LEVEL4 = 'backgrounds/level4.jpg'
LEVEL5 = 'backgrounds/level5.jpg'
LEVEL6 = 'backgrounds/level6.jpg'
LEVEL7 = 'backgrounds/level7.jpg'
LEVEL8 = 'backgrounds/level8.jpg'
LEVEL9 = 'backgrounds/level9.jpg'
LEVEL10 = 'backgrounds/level10.jpg'

# Chair:
CHAIR = 'images/cadeira.png'

# Logos:
GO = 'images/Go.png'
PAUSE = 'images/pause.png'
UFCG_LOGO = 'images/LOGO_UFCG.png'
DRAW_GAME = 'images/empate.png'
GET_READY = 'images/next_level.png'

# Game rounds:
ROUND1 = 'images/round1.png'
ROUND2 = 'images/round2.png'
ROUND3 = 'images/round3.png'
ROUND4 = 'images/round4.png'
ROUND5 = 'images/round5.png'
ROUND6 = 'images/round6.png'
ROUND7 = 'images/round7.png'
ROUND8 = 'images/round8.png'
ROUND9 = 'images/round9.png'
ROUND10 = 'images/round10.png'

# Fonts:
FONT1 = 'fonts/bayoc__.ttf'
FONT2 = 'fonts/bigsky.ttf'
FONT3 = 'fonts/boris_black_boxx.ttf'
