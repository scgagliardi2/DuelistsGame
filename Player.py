import pygame
import Map
import Spellbook
import Spell


class Player:

    # base player speed
    Speed = 3

    def __init__(self, ImagePath, x, y, width, heigth):
        self.Width = width
        self.Height = heigth
        # create player image
        ObjectImage = pygame.image.load(ImagePath)
        # scale image
        self.image = pygame.transform.scale(
            ObjectImage, (self.Width, self.Height))
        self.Facing = "up"
        # Spellbook that player has access to
        CreateSpellBook = Spellbook.Spellbook()
        self.SpellBook = CreateSpellBook.spellbook
        self.Spell1 = self.SpellBook['Blast']
        self.Spell1.KeyBinding = "1"
        self.Spell2 = self.SpellBook['Barrier']
        self.Spell2.KeyBinding = "2"
        self.Spell3 = self.SpellBook['Water Prison']
        self.Spell3.KeyBinding = "3"
        self.Spell4 = self.SpellBook['Lightfoot']
        self.Spell4.KeyBinding = "4"

        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(450, 450)
        self.set_target((450, 450))

    # draw player image to screen
    def draw(self, background, map):
        background.blit(self.image, (self.pos))

    # get destination vector from mouse right click
    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

    # move player and update image if necessary
    def update(self):
        # creat move vector and move
        move = self.target - self.pos
        move_length = move.length()
        if move_length < self.Speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.Speed
            self.pos += move
        
            # check direction of movement and update image
            if abs(move[0]) > abs(move[1]):
                if move[0] >= 0:
                    ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Right Face.png')
                    self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                    self.Facing = "right"
                else:
                    ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Left Face.png')
                    self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                    self.Facing = "left"
            else:
                if move[1] >= 0:
                    ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Front Face.png')
                    self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                    self.Facing = "down"
                elif move[1] < 0:
                    ObjectImage = pygame.image.load('Images/Wizard Sprite/Wizard Back Face.png')
                    self.image = pygame.transform.scale(ObjectImage, (self.Width, self.Height))
                    self.Facing = "up"

        self.rect.topleft = list(int(v) for v in self.pos)