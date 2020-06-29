import pygame
import random

pygame.init()

"The probabilities of every tier you can roll for each level"
p1 = [1,0,0,0,0]
p2 = [1,0,0,0,0]
p3 = [0.75,0.25,0,0,0]
p4 = [0.55,0.3,0.15,0,0]
p5 = [0.4,0.35,0.2,0.05,0]
p6 = [0.25,0.35,0.3,0.1,0]
p7 = [0.19,0.3,0.35,0.15,0.01]
p8 = [0.14,0.2,0.35,0.25,0.06]
p9 = [0.10,0.15,0.3,0.3,0.15]
probability = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

"Set of pokemons in the respective tier"
tier1 = ["Weedle", "Pidgeotto", "Nidoran m", "Nidoran f", "Poliwag"]
tier2 = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Machop"]
tier3 = ["Pikachu", "Abra", "Shellder", "Dratini", "Vulpix"]
tier4 = ["Venonat", "Tentacool", "Pontya", "Seel", "Mankey"]
tier5 = ["Moltres", "Zapdos", "Articuno", "Mewtwo", "Mew"]
tier = [tier1, tier2, tier3, tier4, tier5]

# --- class ---

class Button(object):

    def __init__(self, position, size):

        # create 6 images
        self._images = [
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
        ]

        # fill images with color - grey, green, blue, violet, gold, dark grey
        self._images[0].fill((211, 211, 211))
        self._images[1].fill((0, 128, 0))
        self._images[2].fill((0, 0, 200))
        self._images[3].fill((238, 130, 238))
        self._images[4].fill((255, 223, 0))
        self._images[5].fill((60, 60, 60))

        # get image size and position
        self._rect = pygame.Rect(position, size)

        # select first image
        self._level = 1
        self.index = random.choices([0, 1, 2, 3, 4],probability[self._level-1])
        self.index = self.index[0]

        # random generate a color when reroll
    def generate_random(self):
        self.index = random.choices([0, 1, 2, 3, 4],probability[self._level-1])
        self.index = self.index[0]

    def draw(self, screen):
        # draw selected image
        screen.blit(self._images[self.index], self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked to dark grey
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self.index = 5 # change image


class Roll(object):

    def __init__(self,position,size):

        self._image = [pygame.Surface(size),pygame.Surface(size)]

        self._image[0].fill((0,0,230))
        self._image[1].fill((0, 0, 150))

        self._rect = pygame.Rect(position, size)

        self._index = 0
        self.reroll_button_pressed = False

    def draw(self, screen):
        screen.blit(self._image[self._index], self._rect)


    def onclick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._rect.collidepoint(event.pos):
                    self._index = 1
                    self.need_to_reroll()
        elif event.type == pygame.MOUSEBUTTONUP:
            self._index = 0


    def need_to_reroll(self):
        self.reroll_button_pressed = True


class Level_up(object):
    def __init__(self,position,size):

        self._image = [pygame.Surface(size),pygame.Surface(size)]

        self._image[0].fill((230,0,0))
        self._image[1].fill((150,0,0))

        self._rect = pygame.Rect(position, size)
        self._level = 1

        self._index = 0

    def draw(self, screen):
        screen.blit(self._image[self._index], self._rect)

    def onclick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._rect.collidepoint(event.pos):
                    self._index = 1
                    if self._level < 9:
                        self._level +=1
        elif event.type == pygame.MOUSEBUTTONUP:
            self._index = 0





# --- main ---

# init


screen = pygame.display.set_mode((530,150))

# create buttons

button1 = Button((5, 45), (100, 100))
button2 = Button((110, 45), (100, 100))
button3 = Button((215, 45), (100, 100))
button4 = Button((320, 45), (100, 100))
button5 = Button((425, 45), (100, 100))
reroll_Button = Roll((490,5),(35,35))
level_up_Button = Level_up((450,5),(35,35))
# mainloop

running = True
main_font = pygame.font.SysFont("comicsans", 30)


while running:
    screen.fill((0,0,0))
    level = level_up_Button._level

    button1._level = level
    button2._level = level
    button3._level = level
    button4._level = level
    button5._level = level



    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- buttons events ---

        button1.event_handler(event)
        button2.event_handler(event)
        button3.event_handler(event)
        button4.event_handler(event)
        button5.event_handler(event)

        reroll_Button.onclick(event)
        level_up_Button.onclick(event)

    # --- draws ---

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)

    reroll_Button.draw(screen)
    level_up_Button.draw(screen)

    if reroll_Button.reroll_button_pressed:
        button1.generate_random()
        button2.generate_random()
        button3.generate_random()
        button4.generate_random()
        button5.generate_random()

        reroll_Button.reroll_button_pressed = False

    # --- level up ---

    level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
    reroll_label = main_font.render("R",1,(255,255,255))
    level_up_label = main_font.render("D", 1, (255, 255, 255))
    probability_label = main_font.render(f"1:{probability[level-1][0]},"
                                         f"2:{probability[level-1][1]},"
                                         f"3:{probability[level-1][2]},"
                                         f"4:{probability[level-1][3]},"
                                         f"5:{probability[level-1][4]}",1,(255,255,255))
    screen.blit(level_label, (10, 10))
    screen.blit(probability_label,(100,10))
    screen.blit(reroll_label,(500,15))
    screen.blit(level_up_label, (460, 15))



    pygame.display.update()

# --- the end ---

pygame.quit()
