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

    def RunGameLoop(self):
        IsGameOver = False
        CastSpell1 = False
        CastSpell2 = False
        CastSpell3 = False
        CastSpell4 = False
        CameraMove = False
        CameraDirection = ""

        # create player
        PlayerChar = Player.Player(
            'Images/Wizard Sprite/Wizard Back Face.png', 250, 250, 30, 33)

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

            # check for "events" like key presses and mouse clicks
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
                    elif event.key == pygame.K_RIGHT:
                        CameraMove = True
                        CameraDirection = "right"
                    elif event.key == pygame.K_LEFT:
                        CameraMove = True
                        CameraDirection = "left"
                    elif event.key == pygame.K_DOWN:
                        CameraMove = True
                        CameraDirection = "down"
                    elif event.key == pygame.K_UP:
                        CameraMove = True
                        CameraDirection = "up"
                elif event.type == pygame.KEYUP:
                    CameraMove = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[2]:
                        PlayerChar.set_target(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
            # print(event) # uncomment to print all events to terminal

            # move camera if called for
            if CameraMove:
                self.map.update_camera(CameraDirection)
                PlayerChar.update_camera(CameraDirection)
                for item in TreeLine:
                    item.update_camera(CameraDirection)

            # draw map background
            self.map.draw()

            # draw terrain
            for item in TreeLine:
                item.draw(self.map.GameScreen)

            # cast any spells used
            if CastSpell1:
                PlayerChar.Spell1.draw(
                    self.map.GameScreen, PlayerChar.pos)
                CastSpell1 = False
            if CastSpell2:
                PlayerChar.Spell2.draw(
                    self.map.GameScreen, PlayerChar.pos)
                CastSpell2 = False
            if CastSpell3:
                PlayerChar.Spell3.draw(
                    self.map.GameScreen, PlayerChar.pos)
                CastSpell3 = False
            if CastSpell4:
                PlayerChar.Spell4.draw(
                    self.map.GameScreen, PlayerChar.pos)
                CastSpell4 = False

            # update player position
            PlayerChar.update()

            # draw the player at the new position
            PlayerChar.draw(self.map.GameScreen)

            # update all game graphics
            pygame.display.update()
            clock.tick(self.TickRate)


pygame.init()

NewGame = Game()
NewGame.RunGameLoop()

pygame.quit()
quit()
