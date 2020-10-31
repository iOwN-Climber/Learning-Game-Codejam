import pygame


class Button:
    def __init__(self, win):
        self.win = win

    def create_button(self, xm, ym, x1, x2, y1, y2):
        """

        :param xm: x pos mouse
        :param ym: y pos mouse
        :param x1: x coordinate pciture left
        :param x2: x coordinate picture right
        :param y1: y coordinate picture top
        :param y2: y coordinate picture bottom

        """
        if x1 < xm < x2:
            if y1 < ym < y2:
                return True
        return False

