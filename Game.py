# gain access to the pygame library
import pygame

# size of game screen
ScreenWidth = 800
ScreenHeight = 800
ScreenTitle = 'Duelists Game'

# RGB Color codes
WhiteColor = (255, 255, 255)
BlackColor = (0, 0, 0)
RedColor = (255, 0, 0)
BlueColor = (0, 0, 255)
GreenColor = (0, 255, 0)
# create game clock
clock = pygame.time.Clock()


class Game:

    # FPS rate
    TickRate = 60

    def __init__(self, width, height, title):
        self.title = title
        self.height = height
        self.wifth = width

        # create game display window
        self.GameScreen = pygame.display.set_mode((width, height))
        # set window color
        self.GameScreen.fill(WhiteColor)
        # set window title
        pygame.display.set_caption(title)

    def RunGameLoop(self):
        IsGameOver = False
        direction = ""

        PlayerChar = PlayerCharacter('Charmander.png', 500, 375, 50, 50)

        # MAIN GAME LOOP
        while not IsGameOver:

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    IsGameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = "up"
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                    elif event.key == pygame.K_RIGHT:
                        direction = "right"
                    elif event.key == pygame.K_LEFT:
                        direction = "left"
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        direction = ""
            # print(event) uncomment to log events

            self.GameScreen.fill(WhiteColor)
            # update player position
            PlayerChar.move(direction)
            # draw the player at the new position
            PlayerChar.draw(self.GameScreen)

            # update all game graphics
            pygame.display.update()
            clock.tick(self.TickRate)


class GameObject:

    def __init__(self, ImagePath, x, y, width, heigth):
        # create player image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(ObjectImage, (100, 100))

        self.xPos = x
        self.yPos = y

        self.width = width
        self.height = heigth

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))


class PlayerCharacter(GameObject):

    Speed = 5

    def __init__(self, ImagePath, x, y, width, heigth):
        super().__init__(ImagePath, x, y, width, heigth)

    def draw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))

    def move(self, direction):
        if direction == "up":
            if self.yPos <= -30:
                pass
            else:
                self.yPos -= self.Speed
        elif direction == "down":
            if self.yPos >= 710:
                pass
            else:
                self.yPos += self.Speed
        elif direction == "left":
            if self.xPos <= -30:
                pass
            else:
                self.xPos -= self.Speed
        elif direction == "right":
            if self.xPos >= 750:
                pass
            else:
                self.xPos += self.Speed


pygame.init()

NewGame = Game(ScreenWidth, ScreenHeight, ScreenTitle)
NewGame.RunGameLoop()

pygame.quit()
quit()


# create player image
# PlayerImage = pygame.image.load('Charmander.png')
# PlayerImage = pygame.transform.scale(PlayerImage, (100, 100))

# draw rectangle
# pygame.draw.rect(GameScreen, RedColor, [350, 350, 100, 100])
# draw circle
# pygame.draw.circle(GameScreen, BlueColor, (400, 400), 20)

# insert Charmander image
# GameScreen.blit(PlayerImage, (300, 300))
