# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame, sys, time, dados
from pygame.locals import *
from player import *
from cadeira import *
from parede import *
from musicas import *
from fases import *
from player2 import *
from powerups import *

pygame.font.init()
font3 = pygame.font.Font(FONT2, 30)
def run_karens_adventure():
	game_display = dados.GAME_SCREEN
		
	# Game objects:
	karen = Karen()
	player2 = Player2()
	chair = Chair()
	music = Musica()
	levels = Levels()
	speed_bonus = Skate_bonus()
	frozen_bonus = Frozen_Enemy()
	reset_bonus = Reset_bonus()
	
	# Game variables
	clock = pygame.time.Clock()
	game_time = event_time = bonus_time = 0.0
	event_bonus_time = final_time_event = final_stage_counter = 0.0
	damage_karen = damage_player2 = 0
	wins_karen = wins_player2 = 0
	level_n = 1
	update_music = True
	pause = unpause = final_event = False 
	player1win = player2win = karen_sit = player2_sit = False
	draw_bonus = level_done = allowed_take_bonus = bonus_on_round = False
	frozen_bonus_activate = speed_bonus_activate = frozen_karen = frozen_player2 = False
	player_with_bonus = power_up = announcemment = None
	walls = levels.load_map(level_n)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					if pause:
						pause = False
						unpause = True
					else:
						pause = True
				elif event.key == K_ESCAPE:
					done = True
		
		if unpause:
			unpause = False
			music.unpause_music()
		if pause:
			music.pause_music()
			game_display.blit(pygame.image.load(dados.PAUSE), (290, 230))
				
		if final_event:
			final_time_event += 0.02
			if winner != None:
				game_display.blit(pygame.image.load(dados.FINAL_BACKGROUND), (0,0))
				game_display.blit(announcemment, (277,200))
				game_display.blit(winner.wins_the_game, (235,255))
				text = font3.render("Pressione ESC para voltar ao menu.", 1, dados.YELLOW)
				game_display.blit(text, (20, 610))
			else:
				game_display.blit(pygame.image.load(dados.FINAL_BACKGROUND), (0,0))
				game_display.blit(pygame.image.load(announcemment), (190,200))
				game_display.blit(karen.wins_the_game, (335, 320))
				game_display.blit(player2.wins_the_game, (415, 320))
				text = font3.render("Pressione ESC para voltar ao menu.", 1, dados.YELLOW)
				game_display.blit(text, (20, 610))
		
			if final_time_event <= 1.0:
				pygame.mixer.music.load(dados.FINAL_MUSIC)
				pygame.mixer.music.play(-1)
				karen.game_over_sound.play()
		
		if level_done:
			final_stage_counter += 0.02
			if final_stage_counter <= 3.0:
				game_display.blit(pygame.image.load(dados.GET_READY), (100,400))
			else:
				frozen_bonus_activate = speed_bonus_activate = frozen_karen = frozen_player2 = False
				karen.speed = player2.speed = 3
				level_n += 1
				walls = levels.load_map(level_n)
				game_time = 0.0
				final_stage_counter = 0.0
				level_done = False
				karen_sit = player2_sit = False
			
		if not pause and not (final_event or level_done):
			# Choose the background from the Levels class.
			game_round = levels.count_game_rounds(level_n)
			background = levels.background(level_n)
			game_display.blit(background, (0,0))
			game_display.blit(game_round, (340,10))
			game_time += 0.02
			if game_time >= 2.0:
				karen_sit = player2_sit = False
					
			if levels.bonus < 5:
				power_up = speed_bonus
			elif levels.bonus >=5 and levels.bonus <= 10:
				power_up = frozen_bonus
			elif levels.bonus > 10 and levels.bonus <= 15:
				power_up = reset_bonus
			else:
				power_up = None
				
			for wall in walls:
				if game_time <= 0.08 and pygame.sprite.collide_rect(karen, wall):
					karen.update_position()
				if game_time <= 0.08 and pygame.sprite.collide_rect(player2, wall):
					player2.update_position()
				if not karen_sit:
					karen.collide_detect_karen(wall)
				if not player2_sit:
					player2.collide_detect(wall)
				chair.chair_on_the_wall(wall)
				if power_up != None:
					power_up.bonus_on_the_wall(wall)
				
			music_stops = music.stop_music(game_time)
				
			levels.draw_map(game_display, walls)
				
			if music_stops:
				chair.draw(game_display)
				karen.draw(game_display, damage_karen, wins_karen, karen_sit)
				player2.draw(game_display, damage_player2, wins_player2, player2_sit)
				karen.update(False, frozen_karen, karen_sit)
				player2.update(False, frozen_player2, player2_sit)
				if event_time <= 1.0:
					chair.show_up_sound.play()
					event_time += 0.02
					game_display.blit(chair.logo_GO, (250, 200))
			else:
				karen.update(True, frozen_karen, karen_sit)
				karen.draw(game_display, damage_karen, wins_karen, karen_sit)
				player2.update(True, frozen_player2, player2_sit)
				player2.draw(game_display, damage_player2, wins_player2, player2_sit)
				
			if karen.x <= -10 or karen.x >= 790 or karen.y <= 74 or karen.y >= 630:
				karen.update_position()
			
			if player2.x <= -10 or player2.x >= 790 or player2.y <= 74 or player2.y >= 630:
				player2.update_position()
					
			if power_up != None:
				player_gets_bonus = power_up.get_bonus(karen, player2)
					
				if power_up.show_bonus(game_time):
					event_bonus_time += 0.02
					
					if event_bonus_time <= 0.04 and not allowed_take_bonus:
						power_up.powerup_showup_sound.play()
				
					if not bonus_on_round:
						power_up.bonus_on_the_game(game_display)
						allowed_take_bonus = True
					
				if player_gets_bonus and allowed_take_bonus:
					power_up.powerup_sound.play()
					player_with_bonus = player_gets_bonus[1]
					power_up.powerup_sound.play()
					bonus_on_round = True
					allowed_take_bonus = False
					power_up.rect = pygame.Rect(0, 0, 0, 0)
					
					if levels.bonus < 5:
						speed_bonus_activate = True
					elif levels.bonus >= 5 and levels.bonus <= 10:
						frozen_bonus_activate = True
					elif levels.bonus > 10 and levels.bonus <= 15:
						bonus_time = 0.0
						event_bonus_time = 0.0
						karen.img = karen.walking_down[0]; player2.img = player2.walking_down[0]
						karen.speed = 3
						player2.speed = 3
						bonus = False
						update_music = True
						chair.update_position()
						game_time = 0.09
					else:
						pass
						
				if speed_bonus_activate:
					if player_with_bonus == 'karen':
						karen.speed = karen.speed_bonus
					elif player_with_bonus == 'player2':
						player2.speed = player2.speed_bonus
					else:
						pass
				elif frozen_bonus_activate:
					if player_with_bonus == 'karen':
						player2.speed = 0
						frozen_player2 = True
					elif player_with_bonus == 'player2':
						karen.speed = 0
						frozen_karen = True
					else:
						pass
							
				if frozen_bonus_activate or speed_bonus_activate:
					bonus_time += 0.02
					if bonus_time >= power_up.max_time_bonus:
						frozen_bonus_activate = speed_bonus_activate = False
						frozen_karen = frozen_player2 = False
						player_with_bonus = None
						power_up.update_bonus_position
						bonus_time = 0.0
						karen.img = karen.walking_down[0]; player2.img = player2.walking_down[0]
						karen.speed = 3
						player2.speed = 3
						power_up.powerup_over_sound.play()
				
			if not frozen_bonus_activate and (not (karen_sit or player2_sit)):
				karen.collide_player(player2)
				player2.collide_player(karen)
					
			if update_music:
				if power_up != None:
					power_up.update_bonus_position()
					power_up.rect = pygame.Rect(0, 0, 0, 0)
				bonus_on_round = False
				levels.bonus = random.randint(0,25)
				music.update()
				music.play_music(game_time)
				update_music = False
				event_time = 0.0
					
			collide_result = chair.collide_detect(karen, player2, (not music_stops), event_time)
				
			if collide_result:
				if collide_result[1] == karen:
					karen.x = chair.x
					karen.y = chair.y - 17
					karen_sit = True
					player1win = True
				else:
					player2.x = chair.x
					player2.y = chair.y - 17
					player2_sit = True
					player2win = True
						
				if player1win:
					damage_player2 += 1
				elif player2win:
					damage_karen += 1
						
				player1win = player2win = False
						
				if damage_karen == 3 or damage_player2 == 3:
					game_display.blit(background, (0,0))
					game_display.blit(game_round, (340,10))
					levels.draw_map(game_display, walls)
					karen.draw(game_display, damage_karen, wins_karen, karen_sit)
					player2.draw(game_display, damage_player2, wins_player2, player2_sit)
					level_done = True
					karen.update_position()
					player2.update_position()
					if damage_karen == 3:
						game_display.blit(player2.flag_winner, (280, 200))
						wins_player2 += 1
					elif damage_player2 == 3:
						game_display.blit(karen.flag_winner, (280, 200))
						wins_karen += 1
			
					damage_karen = damage_player2 = 0
				
				if (wins_karen + wins_player2 == 10) or wins_karen == 10 or wins_player2 == 10:
					level_done = False
					if wins_karen > wins_player2:
						victories = wins_karen
						winner = karen
						announcemment = karen.flag_winner
					elif wins_karen == wins_player2:
						winner = None
						announcemment = dados.DRAW_GAME
					else:
						victories = wins_player2
						winner = player2
						announcemment = player2.flag_winner
					final_event = True
				
				if power_up != None:
					power_up.update_bonus_position
				frozen_bonus_activate = speed_bonus_activate = False
				frozen_karen = frozen_player2 = False
				player_with_bonus = None
				bonus_time = 0.0
				event_bonus_time = 0.0
				karen.img = karen.walking_down[0]; player2.img = player2.walking_down[0]
				karen.speed = 3
				player2.speed = 3
				bonus = False
				update_music = True
				chair.update_position()
				game_time = 0.09
			
		pygame.display.flip()
		clock.tick(60)
