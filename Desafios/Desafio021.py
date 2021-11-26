# Faça um programa em Python que abra e reproduza o áudio de arquivo MP3.
from pygame import mixer

mixer.init()
mixer.music.load('ArianneEstreladaManha.mp3')
mixer.music.play()
input('Agora voce escuta?')
