import pygame


class Homescreen:

    def __init__(self, win, width, height, bg, home_w1, home_w2, home_w3):
        self.win = win
        self.width = width
        self.height = height
        self.bg = bg
        self.home_w1 = home_w1
        self.home_w2 = home_w2
        self.home_w3 = home_w3

    def word1_hover(self):
        self.win.blit(self.home_w1, (0, 0))

    def word2_hover(self):
        self.win.blit(self.home_w2, (0, 0))

    def word3_hover(self):
        self.win.blit(self.home_w3, (0, 0))

    def draw(self):
        self.win.blit(self.bg, (0, 0))
