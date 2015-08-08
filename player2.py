# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame
import dados
import random
from pygame.locals import *
from parede import *

class Player2(pygame.sprite.Sprite):
	   
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(1,700)
		self.y = random.randint(70,570)
		self.speed = 3
		self.speed_bonus = 5
		self.img = pygame.image.load(dados.PLAYER2)
		self.rect = pygame.Rect(self.x, self.y, 26, 45)
		self.img_speed_init = 14
		self.img_speed = self.img_speed_init
		self.img_pos = 0
		self.wins_the_game = pygame.image.load(dados.PLAYER2_WINS)
		self.sit_chair = pygame.image.load(dados.PLAYER2_SIT)
		self.flag_winner = pygame.image.load(dados.PLAYER2_FLAG)
		self.frozen = pygame.image.load(dados.FROZEN_PLAYER2)
		self.life = [pygame.image.load(dados.P2_3LIFES), pygame.image.load(dados.P2_2LIFES), pygame.image.load(dados.P2_1LIFE)]
		self.wins = [pygame.image.load(dados.ONE_VICTORY), pygame.image.load(dados.TWO_VICTORIES), 
					 pygame.image.load(dados.THREE_VICTORIES), pygame.image.load(dados.FOUR_VICTORIES),
					 pygame.image.load(dados.FIVE_VICTORIES), pygame.image.load(dados.SIX_VICTORIES),
					 pygame.image.load(dados.SEVEN_VICTORIES), pygame.image.load(dados.EIGHT_VICTORIES),
					 pygame.image.load(dados.NINE_VICTORIES), pygame.image.load(dados.TEN_VICTORIES)]
		self.dancing = [pygame.image.load(dados.PLAYER2_DANCING1), pygame.image.load(dados.PLAYER2_DANCING2),
						 pygame.image.load(dados.PLAYER2_DANCING3)]
		self.walking_down = [pygame.image.load(dados.PLAYER2), pygame.image.load(dados.PLAYER2_DOWN1),
							 pygame.image.load(dados.PLAYER2_DOWN2)]
		self.walking_left = [pygame.image.load(dados.PLAYER2_LEFT), pygame.image.load(dados.PLAYER2_LEFT1), 
							 pygame.image.load(dados.PLAYER2_LEFT2)]
		self.walking_right = [pygame.image.load(dados.PLAYER2_RIGHT), pygame.image.load(dados.PLAYER2_RIGHT1),
							  pygame.image.load(dados.PLAYER2_RIGHT2)]
		self.walking_up = [pygame.image.load(dados.PLAYER2_BACK), pygame.image.load(dados.PLAYER2_UP1),
						   pygame.image.load(dados.PLAYER2_UP2)]
		self.img_max = len(self.dancing) -1
		
	def update(self, music_playing, frozen, sit):
		if sit:
			self.img = self.sit_chair
			return None
			
		if frozen:
			self.img = self.frozen
			return None
		else:
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[K_a] and self.x >= -1:
				if not music_playing:
					self.img_speed -= 4
					if self.img_speed <= 0 and not music_playing:
						self.img = self.walking_left[self.img_pos]
						self.img_speed = self.img_speed_init
						
						if self.img_pos == self.img_max:
							self.img_pos = 0
						else:
							self.img_pos += 1
				self.x -= self.speed
						
			elif keys_pressed[K_d] and self.x <= 780:
				if not music_playing:
					self.img_speed -= 4
					if self.img_speed <= 0 and not music_playing:
						self.img = self.walking_right[self.img_pos]
						self.img_speed = self.img_speed_init
						if self.img_pos == self.img_max:
							self.img_pos = 0
						else:
							self.img_pos += 1
				self.x += self.speed
			elif keys_pressed[K_w] and self.y >= 64:
				if not music_playing:
					self.img_speed -= 4
					if self.img_speed <= 0 and not music_playing:
						self.img = self.walking_up[self.img_pos]
						self.img_speed = self.img_speed_init
						if self.img_pos == self.img_max:
							self.img_pos = 0
						else:
							self.img_pos += 1
				self.y -= self.speed
			elif keys_pressed[K_s] and self.y <= 620:
				if not music_playing:
					self.img_speed -= 4
					if self.img_speed <= 0 and not music_playing:
						self.img = self.walking_down[self.img_pos]
						self.img_speed = self.img_speed_init
						if self.img_pos == self.img_max:
							self.img_pos = 0
						else:
							self.img_pos += 1
				self.y += self.speed
			
			if music_playing:
				self.img_speed -= 2
				if self.img_speed <= 0:
					self.img = self.dancing[self.img_pos]
					self.img_speed = self.img_speed_init
					if self.img_pos == self.img_max:
						self.img_pos = 0
					else:
						self.img_pos += 1
			self.rect = pygame.Rect(self.x, self.y, 28, 45)
		 
	def draw(self, display, damage, wins, sit):
		if sit:
			self.img = self.sit_chair
		display.blit(self.img, (self.x, self.y))
		if damage == 3:
			pass
		else:
			display.blit(self.life[damage], (530,0))
		if wins > 0:
			display.blit(self.wins[wins-1], (650,5))
			
	def collide_detect(self, wall):
		if pygame.sprite.collide_rect(self, wall):
			if self.rect.colliderect(wall.rect):
				# detecta colisão à esquerda
				if ((self.rect.right >= (wall.rect.left)) and (self.rect.left < wall.rect.left)):
					self.x -= self.speed
				
				# detecta colisão à direita
				if ((self.rect.left <= wall.rect.right) and (self.rect.right > wall.rect.right)):
					self.x += self.speed
				
				# detecta colisão no topo
				if ((self.rect.top <= wall.rect.bottom) and (self.rect.bottom > wall.rect.bottom)):
					self.y += self.speed
				
				# detecta colisão na parte inferior
				if ((self.rect.bottom >= (wall.rect.top)) and (self.rect.top < wall.rect.bottom - 10)):
					self.y -= self.speed
				
	def collide_player(self, player2):
		if self.rect.colliderect(player2.rect):
			# detecta colisão à esquerda
			if ((self.rect.right >= (player2.rect.left)) and (self.rect.left < player2.rect.left)):
				self.x -= (self.speed -1)
			
			# detecta colisão à direita
			if ((self.rect.left <= player2.rect.right) and (self.rect.right > player2.rect.right)):
				self.x += (self.speed -1)
			
			# detecta colisão no topo
			if ((self.rect.top <= player2.rect.bottom) and (self.rect.bottom > player2.rect.bottom)):
				self.y += (self.speed -1)
			
			# detecta colisão na parte inferior
			if ((self.rect.bottom >= (player2.rect.top)) and (self.rect.top < player2.rect.bottom - 10)):
				self.y -= (self.speed -1)

	def update_position(self):
		self.x = random.randint(1,700)
		self.y = random.randint(70,570)
