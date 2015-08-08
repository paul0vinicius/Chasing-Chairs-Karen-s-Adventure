# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import sys, pygame, dados
import os
from pygame.locals import *
from main import *

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption("Chasing Chairs: Karen's Adventure")
game_screen = dados.GAME_SCREEN
background = pygame.image.load(dados.BACKGROUND_MENU)
font = pygame.font.Font(FONT1, 60)
font2 = pygame.font.Font(FONT2, 40)
font3 = pygame.font.Font(FONT2, 30)

clock = pygame.time.Clock()

def selection_menu(value):
	if value == 0:
		text = font2.render("Play", 1, dados.YELLOW)
		game_screen.blit(text, (30,580))
	elif value == 10:
		run_karens_adventure()
		return True
	elif value == 1:
		text = font2.render("Como jogar", 1, dados.YELLOW)
		game_screen.blit(text, (180,580))
	elif value == 11:
		text = font.render("Como jogar:", 1, dados.WHITE)
		game_screen.blit(text, (20, 10))
		text = font3.render("Karen", 1, dados.WHITE)
		game_screen.blit(text, (65, 110))
		game_screen.blit(pygame.image.load(dados.KAREN_WINS), (82, 150))
		game_screen.blit(pygame.image.load(dados.KAREN_KEYBOARD), (50, 200))
		text = font3.render("Inimiga", 1, dados.WHITE)
		game_screen.blit(text, (270, 110))
		game_screen.blit(pygame.image.load(dados.PLAYER2_WINS), (300, 150))
		game_screen.blit(pygame.image.load(dados.PLAYER2_KEYBOARD), (265, 200))
		text = font3.render("Ice Bonus", 1, dados.WHITE)
		game_screen.blit(text, (450, 110))
		game_screen.blit(pygame.image.load(dados.ICE), (500, 150))
		text = font3.render("Speed Bonus", 1, dados.WHITE)
		game_screen.blit(text, (600, 110))
		game_screen.blit(pygame.image.load(dados.SKATE), (660, 160))
		text = font3.render("Reset Bonus", 1, dados.WHITE)
		game_screen.blit(text, (610, 220))
		game_screen.blit(pygame.image.load(dados.RESET_BONUS), (660, 260))
		text = font3.render("A musica toca durante um intervalo de tempo e quando a", 1, dados.WHITE)
		game_screen.blit(text, (20, 350))
		text = font3.render("musica parar, os jogadores tem que correr ate a cadeira.", 1, dados.WHITE)
		game_screen.blit(text, (20, 380))
		text = font3.render("Quem pegar a cadeira primeiro tira uma vida do adversario.", 1, dados.WHITE)
		game_screen.blit(text, (20, 410))
		text = font3.render("Cada round possui 3 rodadas e o ganhador do round leva", 1, dados.WHITE)
		game_screen.blit(text, (20, 450))
		text = font3.render("o trofeu do nivel. O jogo possui 10 niveis e vence o jogador", 1, dados.WHITE)
		game_screen.blit(text, (20, 480))
		text = font3.render("com mais trofeus.", 1, dados.WHITE)
		game_screen.blit(text, (20, 510))
		text = font3.render("Pressione Enter ou ESC para voltar ao menu.", 1, dados.YELLOW)
		game_screen.blit(text, (20, 610))
		text = font3.render("Pressione espaco para pausar o jogo.", 1, dados.WHITE)
		game_screen.blit(text, (20, 580))
		
		pygame.display.update()
		pygame.display.flip()
		return True
	elif value == 2:
		text = font2.render("Criadores", 1, dados.YELLOW)
		game_screen.blit(text, (460,580))
	elif value == 12:
		text = font.render("Criadores:", 1, dados.WHITE)
		game_screen.blit(text, (20, 10))
		text = font3.render("Paulo Vinicius Soares", 1, dados.WHITE)
		game_screen.blit(text, (20, 110))
		game_screen.blit(pygame.image.load(dados.UFCG_LOGO), (590, 10))
		text = font3.render("Mariana Melo", 1, dados.WHITE)
		game_screen.blit(text, (20, 140))
		text = font.render("Monitores:", 1, dados.WHITE)
		game_screen.blit(text, (20, 300))
		text = font3.render("Roberto Matheus", 1, dados.WHITE)
		game_screen.blit(text, (20, 400))
		text = font3.render("Klaudio Medeiros", 1, dados.WHITE)
		game_screen.blit(text, (20, 430))
		text = font3.render("Pressione Enter ou ESC para voltar ao menu.", 1, dados.YELLOW)
		game_screen.blit(text, (20, 610))
		
		pygame.display.update()
		pygame.display.flip()
		return True
	elif value ==  3:
		text = font2.render("Sair", 1, dados.YELLOW)
		game_screen.blit(text, (680 ,580))
	elif value == 13:
		exit()

# Starts Menu Music:
pygame.mixer.music.load(dados.MENU_MUSIC)
pygame.mixer.music.play(-1)

enter = False
valor = 0
while True:
	clock.tick(60)
	game_screen.blit(background, (0,0))

	if valor < 10:
		text = font.render("chasing chairs:", 1, dados.WHITE)
		game_screen.blit(text, (100, 10))
		text = font.render("Karen's adventure", 1, dados.WHITE)
		game_screen.blit(text, (30, 80))
		text = font2.render("Play", 1, dados.WHITE)
		game_screen.blit(text, (30,580))
		text = font2.render("Como jogar", 1, dados.WHITE)
		game_screen.blit(text, (180,580))
		text = font2.render("Criadores", 1, dados.WHITE)
		game_screen.blit(text, (460,580))
		text = font2.render("Sair", 1, dados.WHITE)
		game_screen.blit(text, (680 ,580))
	
	if valor <= 0 or valor > 13:
		valor = 0
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(0)
			break
		elif event.type == pygame.KEYDOWN:
			if not entrou_submenu:
				if event.key == pygame.K_RIGHT:
					valor += 1
				elif event.key == pygame.K_LEFT:
					valor -= 1
			if valor == 4 and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
				valor = 0
			elif event.key == pygame.K_ESCAPE:
				valor -= 10
			elif event.key == pygame.K_RETURN:
				enter = True
				valor += 10
	
	entrou_submenu = selection_menu(valor)
	if enter and valor == 10:
		pygame.mixer.music.load(dados.MENU_MUSIC)
		pygame.mixer.music.play(-1)
		valor = 0
		enter = False
		
	pygame.display.update()
	pygame.display.flip()
