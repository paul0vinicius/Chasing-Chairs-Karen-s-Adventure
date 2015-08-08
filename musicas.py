# coding: utf-8
# Aluno 1: Paulo Vinícius da Silva Soares - Matrícula: 114110478
# Aluno 2: Maria Mariana Maia Melo Fernandes - Matrícula: 114110468
# Projeto de Programação I - UFCG - 2014.1
# Chasing Chairs: Karen's Adventure
# 12/09/2014

import pygame, dados, time, random

class Musica():
	
	def __init__(self):
		self.playlist = dados.PLAYLIST
		self.playlist_number = random.randint(0, len(dados.PLAYLIST) -1)
		self.music = self.playlist[self.playlist_number]
		self.music_time = random.randint(5, 20)
		
	def update(self):
		self.check_if_its_repeated = self.playlist_number
		self.playlist_number = random.randint(0, len(dados.PLAYLIST) -1)
		while self.check_if_its_repeated == self.playlist_number:
			self.playlist_number = random.randint(0, len(dados.PLAYLIST) -1)
		self.music = self.playlist[self.playlist_number]
		self.music_time = random.randint(5, 20)
		pygame.mixer.music.load(self.music)
			
	def play_music(self, time_event_music):
		if time_event_music <= 0.5:
			pygame.mixer.music.play()
			
	def pause_music(self):
		pygame.mixer.music.pause()
	
	def unpause_music(self):
		pygame.mixer.music.unpause()
		
	def stop_music(self, time_event_music):
		if int(time_event_music) >= self.music_time:
			pygame.mixer.music.stop()
			return True
