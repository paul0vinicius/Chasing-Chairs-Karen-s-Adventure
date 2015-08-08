# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame, random, dados
from player import *
from player2 import *
from parede import *
from fases import *

class Skate_bonus(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.img = pygame.image.load(dados.SKATE)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		self.max_time_bonus = random.randint(5, 10)
		self.time_bonus_show_up = random.randint(3, 15)
		self.powerup_showup_sound = pygame.mixer.Sound(dados.SHOES_BONUS)
		self.powerup_sound = pygame.mixer.Sound(dados.PLAYER_GETS_BONUS)
		self.powerup_over_sound = pygame.mixer.Sound(dados.BONUS_OVER)
		
	def bonus_on_the_game(self, display):
		display.blit(self.img, (self.x, self.y))
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
			
	def bonus_on_the_wall(self, wall):
		if self.rect.colliderect(wall.rect):
			self.x = random.randint(1,700)
			self.y = random.randint(70, 570)
		
	def get_bonus(self, player, player2):
		if pygame.sprite.collide_rect(self, player):
			return True, 'karen'
		elif pygame.sprite.collide_rect(self, player2):
			return True, 'player2'
		else:
			return False

	def show_bonus(self, game_time):
		if int(game_time) >= self.time_bonus_show_up:
			return True
			
	def update_bonus_position(self):
		self.time_bonus_show_up = random.randint(3, 15)
		self.max_time_bonus = random.randint(5, 10)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)

class Frozen_Enemy(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.img = pygame.image.load(dados.ICE)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		self.max_time_bonus = random.randint(5, 10)
		self.time_bonus_show_up = random.randint(3, 15)
		self.powerup_showup_sound = pygame.mixer.Sound(dados.ICE_BONUS)
		self.powerup_sound = pygame.mixer.Sound(dados.PLAYER_GETS_BONUS)
		self.powerup_over_sound = pygame.mixer.Sound(dados.BONUS_OVER)
		
	def bonus_on_the_game(self, display):
		display.blit(self.img, (self.x, self.y))
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
			
	def bonus_on_the_wall(self, wall):
		if self.rect.colliderect(wall.rect):
			self.x = random.randint(1,700)
			self.y = random.randint(70, 570)
		
	def get_bonus(self, player, player2):
		if pygame.sprite.collide_rect(self, player):
			return True, 'karen'
		elif pygame.sprite.collide_rect(self, player2):
			return True, 'player2'
		else:
			return False

	def show_bonus(self, game_time):
		if int(game_time) >= self.time_bonus_show_up:
			return True
			
	def update_bonus_position(self):
		self.time_bonus_show_up = random.randint(3, 15)
		self.max_time_bonus = random.randint(5, 10)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		
class Reset_bonus(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.img = pygame.image.load(dados.RESET_BONUS)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		self.max_time_bonus = random.randint(5, 10)
		self.time_bonus_show_up = 25.0
		self.powerup_showup_sound = pygame.mixer.Sound(dados.RESET_BONUS_SOUND)
		self.powerup_sound = pygame.mixer.Sound(dados.PLAYER_GETS_BONUS)
		self.powerup_over_sound = pygame.mixer.Sound(dados.BONUS_OVER)
		
	def bonus_on_the_game(self, display):
		display.blit(self.img, (self.x, self.y))
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
			
	def bonus_on_the_wall(self, wall):
		if self.rect.colliderect(wall.rect):
			self.x = random.randint(1,700)
			self.y = random.randint(70, 570)
		
	def get_bonus(self, player, player2):
		if pygame.sprite.collide_rect(self, player):
			return True, 'karen'
		elif pygame.sprite.collide_rect(self, player2):
			return True, 'player2'
		else:
			return False

	def show_bonus(self, game_time):
		if int(game_time) >= self.time_bonus_show_up:
			return True
			
	def update_bonus_position(self):
		self.time_bonus_show_up = random.randint(3, 15)
		self.max_time_bonus = random.randint(5, 10)
		self.x = random.randint(1,700)
		self.y = random.randint(70, 570)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
