import pygame
import random


class VocabularyGame:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, win, width, height, bgv, font):
        self.win = win
        self.width = width
        self.height = height
        self.vocabularies = {"bridge": "Brücke", "spoon": "Löffel", "car": "Auto", "subtitle": "Untertitel",
                             "nose": "Nase", "pencil": "Bleistift", "desk": "Tisch", "teacher": "Lehrer"}
        self.bgv = bgv
        self.guessed = ""
        self.font = font
        self.word = random.choice(list(self.vocabularies.keys()))
        self.count = 0
        self.won = False
        self.win_text = self.font.render("Correct!", 1, self.BLACK)

    def activate_home(self):
        if self.won:
            self.won = False
            return True
        return False

    def to_guess(self):
        text = self.font.render(str(self.word), 1, self.BLACK)
        self.win.blit(text, (230, 280))

    def getinput(self, user_input):
        if user_input != "minus":
            self.guessed += user_input
        else:
            self.guessed = self.guessed[0:-1]

    def check(self):
        if self.guessed == self.vocabularies[self.word]:
            self.count += 1
            del self.vocabularies[self.word]
            self.win.blit(self.win_text, (230, 480))
            pygame.display.update()
            self.guessed = ""
            self.word = random.choice(list(self.vocabularies.keys()))
            pygame.time.delay(1000)
        else:
            loose_texxt = self.font.render("Wrong!", 1, self.BLACK)
            self.win.blit(loose_texxt, (230, 480))
            pygame.display.update()
            self.guessed = ""
            self.word = random.choice(list(self.vocabularies.keys()))
            pygame.time.delay(1000)

    def draw(self):
        self.win.blit(self.bgv, (0, 0))
        if self.count < 5:
            self.to_guess()

            guessed_text = self.font.render(self.guessed, True, self.BLACK)
            self.win.blit(guessed_text, (690, 280))

        else:
            win_text = self.font.render("You Won!!!", 1, self.BLACK)
            self.win.blit(win_text, (230, 430))
            pygame.display.update()
            pygame.time.delay(2000)
            self.won = True
            self.count = 0
