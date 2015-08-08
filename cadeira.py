# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame,random, sys, time
import dados

class Chair(pygame.sprite.Sprite):
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x = random.randint(1,700)
		self.y = random.randint(70,570)
		self.img = pygame.image.load(dados.CHAIR)
		self.rect = pygame.Rect(self.x, self.y, 20, 20)
		self.show_up_sound = pygame.mixer.Sound(dados.SHOW_CHAIR)
		self.logo_GO = pygame.image.load(dados.GO)
		
	def draw(self, display):
		display.blit(self.img, (self.x, self.y))
		
	def update_position(self):
		self.x = random.randint(1,700)
		self.y = random.randint(70,570)
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		
	def collide_detect(self, karen, player2, music_playing, event_time):
		if event_time <= 1.0:
			return False
		if music_playing: # Make sure that the chair will not be taken before music stops.
			return False
		if pygame.sprite.collide_rect(self, karen):
			return True, karen
		elif pygame.sprite.collide_rect(self, player2):
			return True, player2

	def chair_on_the_wall(self, wall):
		if self.rect.colliderect(wall.rect):
			self.update_position()
