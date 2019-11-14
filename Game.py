# gain access to the pygame library
import pygame
import Map
import Player
import Spell
import TerrainObject

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
        PlayerMove = False
        CastSpell1 = False
        CastSpell2 = False
        CastSpell3 = False
        CastSpell4 = False

        PlayerChar = Player.Player('Images/Wizard Sprite/Wizard Back Face.png', 450, 450, 30, 33)

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
                    if event.key == pygame.K_1:
                        CastSpell1 = True
                    elif event.key == pygame.K_2:
                        CastSpell2 = True
                    elif event.key == pygame.K_3:
                        CastSpell3 = True
                    elif event.key == pygame.K_4:
                        CastSpell4 = True
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[2]:
                        PlayerMove = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            # print(event)

            self.map.draw()

            # draw terrain
            for item in TreeLine:
                item.draw(self.map.GameScreen)

            # update player spell cast
            if CastSpell1:
                PlayerChar.Spell1.draw(
                    self.map.GameScreen, (PlayerChar.XPosition), (PlayerChar.YPosition))
                CastSpell1 = False
            if CastSpell2:
                PlayerChar.Spell2.draw(
                    self.map.GameScreen, (PlayerChar.XPosition), (PlayerChar.YPosition))
                CastSpell2 = False
            if CastSpell3:
                PlayerChar.Spell3.draw(
                    self.map.GameScreen, (PlayerChar.XPosition), (PlayerChar.YPosition))
                CastSpell3 = False
            if CastSpell4:
                PlayerChar.Spell4.draw(
                    self.map.GameScreen, (PlayerChar.XPosition), (PlayerChar.YPosition))
                CastSpell4 = False

            # update player position
            if PlayerMove:
                PlayerChar.move(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                PlayerMove = False

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
