import pygame

pygame.init()

WIDTH, HEIGHT = 1300, 700
FPS = 30


# load images
BG = pygame.image.load("assets/Home.png")
HOME_W1 = pygame.image.load("assets/Home_word1.png")
HOME_W2 = pygame.image.load("assets/Home_word2.png")
HOME_W3 = pygame.image.load("assets/Home_word3.png")

# chemie
BGC = pygame.image.load("assets/cchh.png")
BCR = pygame.image.load("assets/cr.png")
BHR = pygame.image.load("assets/eqc.png")
BCW = pygame.image.load("assets/cw.png")

# vocabulary
BGV = pygame.image.load("assets/Voc Screen.png")

# programming
BPS = pygame.transform.scale(pygame.image.load("assets/ps1.png"), (1300, 700))
BPS_a = pygame.transform.scale(pygame.image.load("assets/psa.png"), (1300, 700))
BPS_b = pygame.transform.scale(pygame.image.load("assets/psb.png"), (1300, 700))
BPS_c = pygame.transform.scale(pygame.image.load("assets/psc.png"), (1300, 700))
BPS_l = pygame.transform.scale(pygame.image.load("assets/psl.png"), (1300, 700))

# FONT
FONT = pygame.font.SysFont("helvetica", 45)


