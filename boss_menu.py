from boss import Boss
from the_arrow import levelChanger
class BossMenu:
    def _init_(self):
        ...
        self.blocks = []
        self.fill_boss_info()

    def fill_boss_info(self):
        for i in range(1, 5):
            self.blocks.append(Boss(i, i + 100))
    def fill_boss_changers(self):
        self.blocks.insert(0, levelChanger('left'))
        self.blocks.append(levelChanger('right'))
    def draw_blocks(self, block, screen):
        for blocks in self.blocks:
            block.draw_block(screen)


