import pygame
import sys

pygame.init()

class Main():
    def __init__(self):
        pygame.display.set_caption('teste colisão')
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('passaro.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_position = [160, 260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            img_rect = pygame.Rect(self.img_position[0], self.img_position[1], self.img.get_width(), self.img.get_height())
            if img_rect.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else: 
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            # se segurar os dois botões ao mesmo tempo, se cancela e não move
            self.img_position[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, (self.img_position))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #movimentação
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Main().run()