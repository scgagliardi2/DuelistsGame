# gain access to the pygame library
import pygame
import Map
import Player
import Spell
import TerrainObject

# size of game screen
ScreenWidth = 900
ScreenHeight = 900
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

    def __init__(self):
        self.map = Map.Map()

        pass

    def RunGameLoop(self):
        IsGameOver = False
        direction = ""
        drawFireball = False
        CastSpell1 = False

        PlayerChar = Player.Player('Images/Charmander.png', 500, 375, 30, 30)

        # create line if trees
        TreeLine = [TerrainObject.TerrainObject('Images/Tree.png', 100, 100, 40, 40),
                    TerrainObject.TerrainObject(
                        'Images/Tree.png', 125, 100, 40, 40),
                    TerrainObject.TerrainObject(
                        'Images/Tree.png', 150, 100, 40, 40),
                    TerrainObject.TerrainObject(
                        'Images/Tree.png', 175, 100, 40, 40),
                    TerrainObject.TerrainObject(
                        'Images/Tree.png', 200, 100, 40, 40),
                    TerrainObject.TerrainObject('Images/Tree.png', 225, 100, 40, 40)]

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
                    elif event.key == pygame.K_1:
                        CastSpell1 = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        direction = ""
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # drawFireball = True
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            # print(event)

            self.map.GameScreen.fill(WhiteColor)

            # draw terrain
            for item in TreeLine:
                item.draw(self.map.GameScreen)

            # update player spell cast
            if CastSpell1:
                PlayerChar.Spell1.draw(
                    self.map.GameScreen, (PlayerChar.XPosition), (PlayerChar.YPosition))
                CastSpell1 = False

            # update player position
            PlayerChar.move(direction)

            # draw the player at the new position
            PlayerChar.draw(self.map.GameScreen, self.map)

            # update all game graphics
            pygame.display.update()
            clock.tick(self.TickRate)


pygame.init()

NewGame = Game()
NewGame.RunGameLoop()

pygame.quit()
quit()
