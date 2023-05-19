# Faça um programa em python que abra e produza o áudio de um arquivo MP3.

import pygame 

pygame.init()
pygame.mixer_music.load('musica.mp3')
pygame.mixer_music.play()
pygame.event.wait()