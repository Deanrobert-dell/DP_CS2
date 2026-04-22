#snake game in pygame, 16x16 grid
import pygame
import random
def main():
    pygame.init()
    GRID = 16
    CELL = 30
    WIDTH, HEIGHT = GRID * CELL, GRID * CELL
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    def place_apple(snake):
        while True:
            pos = (random.randrange(0, GRID), random.randrange(0, GRID))
            if pos not in snake:
                return pos

    # initial game state
    snake = [(GRID // 2, GRID // 2), (GRID // 2 - 1, GRID // 2)]
    direction = (1, 0)  # moving right
    apple = place_apple(snake)
    score = 0
    speed = 8
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pygame.K_r and game_over:
                    # restart
                    snake = [(GRID // 2, GRID // 2), (GRID // 2 - 1, GRID // 2)]
                    direction = (1, 0)
                    apple = place_apple(snake)
                    score = 0
                    speed = 8
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        if not game_over:
            # move snake
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # check collisions with walls
            if not (0 <= new_head[0] < GRID and 0 <= new_head[1] < GRID):
                game_over = True
            # check self collision
            elif new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == apple:
                    score += 1
                    apple = place_apple(snake)
                    speed = min(20, speed + 1)
                else:
                    snake.pop()

        # draw
        screen.fill((10, 10, 10))
        # snake
        for i, seg in enumerate(snake):
            color = (50, 200, 50) if i == 0 else (30, 160, 30)
            pygame.draw.rect(screen, color, (seg[0] * CELL, seg[1] * CELL, CELL - 1, CELL - 1))
        # apple
        pygame.draw.rect(screen, (200, 30, 30), (apple[0] * CELL, apple[1] * CELL, CELL - 1, CELL - 1))

        # HUD
        score_surf = font.render(f"Score: {score}", True, (200, 200, 200))
        screen.blit(score_surf, (5, 5))

        if game_over:
            over_surf = font.render("Game Over - Press R to restart or ESC to quit", True, (255, 255, 255))
            rect = over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(over_surf, rect)

        pygame.display.flip()
        clock.tick(speed)

