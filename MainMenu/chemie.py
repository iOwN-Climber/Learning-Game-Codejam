import pygame
from MainMenu.Button import Button
import sys


class Chemie:
    questions = {"FeS + O2 --> Fe3O4 + SO2": "3FeS + 5O2 --> Fe3O4 + 3SO2",
                 "CuO + C --> Cu + CO2": "2CuO + C --> 2Cu + CO2", "Mg + Cu2O --> MgO + Cu": "2CuO + C --> 2Cu + CO2",
                 "FeS + O2 --> Fe2O3 + SO2": "4FeS + 7O2 --> 2Fe2O3 + 4SO2",
                 "Cu2O + Zn --> Cu + ZnO": "Cu2O + Zn --> 2Cu + ZnO",
                 "CuO + Fe --> Fe2O3 + Cu": "3CuO + 2Fe --> Fe2O3 + 3Cu"}
    q_list = list(questions.keys())

    q_list_len = len(q_list)

    user_text = ''

    def __init__(self, win, width, height, bgc, bcr, bhr, bcw, font):
        self.win = win
        self.width = width
        self.height = height

        self.bgc = bgc
        self.bcr = bcr
        self.bhr = bhr
        self.bcw = bcw

        self.font = font
        self.fontc = pygame.font.SysFont("bradley hand itc", 32)
        self.fontx = pygame.font.SysFont("helvetica", 72)

        self.c_checker = 5
        self.count = 0
        self.count_neg = 0
        self.count_pos = 0

        self.index = 0

        self.button = Button(self.win)

    def on_press(self):
        for q in self.q_list:
            cq = self.q_list[self.count]
            q_list_end = self.q_list_len - self.index
            if q_list_end != 1:
                nq = self.index + 1
                text = self.fontc.render(str("Solve the following equation:  " + str(cq)), 1, (255, 255, 255))
                self.win.blit(text, (223, 190))
                txt = self.fontc.render(str("Your Answer:"), True, (255, 255, 255))
                self.win.blit(txt, (223, 372))
            else:
                if self.c_checker == 0:
                    self.win.blit(self.bcw, (0, 0))
                    txt1 = self.fontc.render(f"You scored 0/5 questions right! Try harder next time!", True,
                                             (255, 255, 255))
                    self.win.blit(txt1, (200, 400))
                elif self.c_checker == 10:
                    self.win.blit(self.bcr, (0, 0))
                else:
                    txt1 = self.fontc.render(
                        f"You scored {self.count_pos}/5 questions right and {self.count_neg} questions wrong!", True,
                        (255, 255, 255))
                    self.win.blit(self.bhr, (0, 0))
                    self.win.blit(txt1, (180, 300))

    def check(self):
        if self.user_text == self.questions[self.q_list[0]]:
            self.count += 1
            self.count_pos += 1
            self.c_checker += 1
            self.index += 1
            self.user_text = ""
            right = self.fontc.render("✔", True, (0, 128, 0))
            self.win.blit(right, (180, 450))
            pygame.display.update()
            pygame.time.delay(1000)

        else:
            self.count -= 1
            self.count_neg += 1
            self.c_checker -= 1
            self.index += 1
            self.user_text = ""
            wrong = self.fontx.render("X", True, (255, 0, 0))
            self.win.blit(wrong, (750, 350))
            pygame.display.update()
            pygame.time.delay(1000)

    def getinput(self, user_input):
        if user_input != "minus":
            self.user_text += user_input
        else:
            self.user_text = self.user_text[0:-1]

    def draw(self):
        self.win.blit(self.bgc, (0, 0))
        text_surface = self.fontc.render(self.user_text, True, (255, 255, 255))
        self.win.blit(text_surface, (415, 372))
        self.on_press()
        