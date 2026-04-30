import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("snake")
font = pygame.font.Font(None, 36)

# Create the snake game board 20x20
def draw_board():
    for row in range(20):
        for col in range(20):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, "#a2d049", (col * 50, row * 50, 50, 50))  # light green squares
            else:
                pygame.draw.rect(screen, "#a9d751", (col * 50, row * 50, 50, 50))  # dark green squares

#function for random apple spawn
def spawn_apple():
    apple_x = random.randint(0, 19) * 50 + 25
    apple_y = random.randint(0, 19) * 50 + 25
    return (apple_x, apple_y)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")  # Fill background with color
    draw_board()
    apple_pos = spawn_apple()
    pygame.draw.circle(screen, "red", apple_pos1, 10)  # Draw the apple
    pygame.display.flip()
