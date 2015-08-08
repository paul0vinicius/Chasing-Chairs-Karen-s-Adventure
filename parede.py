# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame, dados

class Wall(pygame.sprite.Sprite):
	def __init__(self, (x, y)):
		pygame.sprite.Sprite.__init__(self)
		self.position = (x, y)
		self.img = pygame.image.load(dados.WALL)
		self.rect = pygame.Rect(self.position, (31, 32))
