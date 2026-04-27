import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base_dir = os.path.dirname(__file__)
        music_dir = os.path.join(base_dir, "music")

        self.playlist = [
            os.path.join(music_dir, "snake.mp3"),
            os.path.join(music_dir, "game.mp3"),

        ]
        
        self.current = 0
        
    def play(self):
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play()

    def play_loop(self):
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play(-1)

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play_loop()

    def game_over(self):
        pygame.mixer.music.load(self.playlist[1]) 
        pygame.mixer.music.play(0)

    def stop(self):
        pygame.mixer.music.stop()