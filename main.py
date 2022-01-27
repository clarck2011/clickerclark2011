import pygame
from the_arrow import levelChanger
from boss_menu import BossMenu
class Main:
    def __init__(self):
        self.WINDOW_WIDTH = 600
        self.WINDOW_HIGHT = 400
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HIGHT))
        self.screen.fill((0, 0, 255))
        self.boss_menu = BossMenu()
    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
    def draw(self, screen):
        self.boss_menu.draw_blocks(self, screen)
        pygame.display.flip()

main = Main()
main.launch()
