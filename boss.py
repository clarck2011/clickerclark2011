import pygame.image
class Boss:
    def _init_(self, level, block_pos):
        self.font = pygame.font.SysFont('ariel', 30)
        self.block_picture = self.fontrender(str(level)), False , (0, 0, 255)
        self.level = level
        self.healph = self.level + self.level % 2
        self.gold = self.healph/2
        self.picture = pygame.image.load('img/boss.png')
        self.block_pos = (block_pos + 30, 30)
        self.pos = (100, 100)
    def draw_block(self, screen):
        screen.blit(self.block_picture, self.pos)