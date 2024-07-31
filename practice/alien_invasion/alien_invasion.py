import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        pygame.init()

        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键鼠
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()

            # 可见屏幕
            pygame.display.flip()

if __name__=='__main__':
    # 创建游戏实例
    ai=AlienInvasion()
    ai.run_game()
