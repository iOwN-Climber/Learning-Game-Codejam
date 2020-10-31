import pygame
from MainMenu.Button import Button
from MainMenu.constants import WIDTH, HEIGHT, FPS, BG, BGC, FONT, BGV, BCR, HOME_W1, HOME_W2, HOME_W3, BCW, BHR, BPS, \
    BPS_a, BPS_b, BPS_c, BPS_l
from MainMenu.home_menu import Homescreen
from MainMenu.chemie import Chemie
from Vocabulary.vocabulary import VocabularyGame
from Programming.programming import Programming

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lernhilfe")


def main():
    # home screen
    hs = True
    w1, w2, w3 = False, False, False

    # chemie screen
    cs = False

    # vocabulary screen
    vs = False

    # programming screen
    ps = False

    # Class setup
    home = Homescreen(WIN, WIDTH, HEIGHT, BG, HOME_W1, HOME_W2, HOME_W3)
    chemie = Chemie(WIN, WIDTH, HEIGHT, BGC, BCR, BHR, BCW, FONT)
    vocabulary = VocabularyGame(WIN, WIDTH, HEIGHT, BGV, FONT)
    programming = Programming(WIN, BPS, BPS_a, BPS_b, BPS_c, BPS_l)
    button = Button(WIN)

    # main Loop variables
    run = True
    clock = pygame.time.Clock()

    programming.update_task_num()
    programming.choose_task()
    while run:
        user_letter_input = ""
        clock.tick(FPS)

        if hs:
            home.draw()
        if cs:
            chemie.draw()
        if vs:
            vocabulary.draw()
        if ps:
            programming.draw()

        if vocabulary.activate_home():
            vs = False
            hs = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_letter_input = "minus"
                    if vs:
                        vocabulary.getinput(user_letter_input)
                    elif cs:
                        chemie.getinput(user_letter_input)

                else:
                    user_letter_input += event.unicode
                    if vs:
                        vocabulary.getinput(user_letter_input)
                    elif cs:
                        chemie.getinput(user_letter_input)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                # button Chemie
                if button.create_button(x, y, 300, 460, 311, 336):
                    hs = False
                    cs = True
                    w1, w2, w3 = False, False, False

                elif button.create_button(x, y, 901, 1101, 408, 479) and cs:
                    chemie.check()

                # button vocabulary
                elif button.create_button(x, y, 300, 400, 191, 220):
                    vs = True
                    hs = False
                    w1, w2, w3 = False, False, False

                elif button.create_button(x, y, 940, 1080, 590, 630) and vs:
                    vocabulary.check()

                # button programming
                elif button.create_button(x, y, 300, 512, 240, 280):
                    hs = False
                    ps = True
                    w1, w2, w3 = False, False, False
                # back to home button
                elif button.create_button(x, y, 20, 120, 20, 120):
                    ps = False
                    hs = True
                    vs = False
                    cs = False


                # programming answers
                elif ps:
                    if button.create_button(x, y, 666, 686, 135, 155):
                        programming.choose_answer(True)

                    elif button.create_button(x, y, 666, 686, 235, 255):
                        programming.choose_answer(False, True)

                    elif button.create_button(x, y, 666, 686, 335, 355):
                        programming.choose_answer(False, False, True)

                    # submit button
                    elif button.create_button(x, y, 890, 1020, 435, 480):
                        programming.check_answer()

            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                if hs:
                    if button.create_button(x, y, 300, 400, 191, 220):
                        w1 = True
                    elif button.create_button(x, y, 300, 512, 240, 280):
                        w2 = True
                    elif button.create_button(x, y, 300, 460, 311, 336):
                        w3 = True
                    else:
                        w1, w2, w3 = False, False, False

        if programming.back_home():
            ps = False
            hs = True

        if w1:
            home.word1_hover()
        elif w2:
            home.word2_hover()
        elif w3:
            home.word3_hover()

        pygame.display.update()

    pygame.quit()


main()
