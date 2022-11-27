import pygame
import os
import random

WIDTH, HEIGHT =  700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cats and Ladders")

WHITE = ((255, 255, 255))
FPS = 60

bg_image = pygame.image.load(os.path.join('assets', 'ladders.jpg'))
bg_size = pygame.transform.scale(bg_image, (700, 700))

cat_path = os.path.join('assets', 'nyan.png')

class Cat(object):  # represents the bird, not the game
    def __init__(self):
        CAT_WIDTH, CAT_HEIGHT = 70, 50
        self.image = pygame.image.load(cat_path)
        self.size = pygame.transform.scale(self.image, (CAT_WIDTH, CAT_HEIGHT))
        # the bird's position
        self.x = 3
        self.y = 640
        self.check = False

    def handle_keys(self):
        speed = 70
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self.check == False:
                self.x += speed
                self.check = True
        elif key[pygame.K_LEFT]:
            if self.check == False:
                self.x -= speed
                self.check = True
        elif key[pygame.K_UP]:
            if self.check == False:
                self.y -= speed
                self.check = True
        elif key[pygame.K_DOWN]:
            if self.check == False:
                self.y += speed
                self.check = True
        elif key[pygame.K_SPACE]:
            if self.check == False:
                num = random.randint(1, 6)
                print(num)
                self.check = True
        else:
            self.check = False

    def draw(self, screen):
        screen.blit(self.size, (self.x, self.y))

cat = Cat()

def draw():
    screen.fill(WHITE)
    screen.blit(bg_size, (0, 0))
    cat.draw(screen)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    x = 5
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        cat.handle_keys()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()
