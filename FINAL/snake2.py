import pygame
import random

# Initialize pygame
pygame.init()

# Setup
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# --- Functions ---
def draw_board():
    for row in range(20):
        for col in range(20):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, "#a2d049", (col * 50, row * 50, 50, 50))
            else:
                pygame.draw.rect(screen, "#a9d751", (col * 50, row * 50, 50, 50))

# Global variables for apple
_apple_pos = None

def spawn_apple():
    global _apple_pos
    if _apple_pos is None:
        # Fixed to align with the 50x50 grid center
        apple_x = random.randint(0, 19) * 50 + 25
        apple_y = random.randint(0, 19) * 50 + 25
        _apple_pos = (apple_x, apple_y)
    return _apple_pos

def eat_apple():
    global _apple_pos
    _apple_pos = None

# snake start
cell = 50
grid = 20
start_x = (grid // 2) * cell
start_y = (grid // 2) * cell
snake_pos = [(start_x, start_y), (start_x - cell, start_y), (start_x - 2 * cell, start_y)]
snake_dir = (cell, 0) # go RIGHTRS

# main func
running = True
while running:
    # each key press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, cell):
                snake_dir = (0, -cell)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -cell):
                snake_dir = (0, cell)
            elif event.key == pygame.K_LEFT and snake_dir != (cell, 0):
                snake_dir = (-cell, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-cell, 0):
                snake_dir = (cell, 0)

    # 2. Update Snake Position
    new_head = (snake_pos[0][0] + snake_dir[0], snake_pos[0][1] + snake_dir[1])
    # Wrap around screen
    new_head = (new_head[0] % (cell * grid), new_head[1] % (cell * grid))
    snake_pos.insert(0, new_head)

    # 3. Collision Check
    apple_center = spawn_apple()
    head_center = (snake_pos[0][0] + cell // 2, snake_pos[0][1] + cell // 2)
    
    if head_center == apple_center:
        eat_apple()
        # Grow: do not pop tail
    else:
        snake_pos.pop()

    # 4. Drawing
    screen.fill("black")
    draw_board()
    
    # Draw apple
    if _apple_pos:
        pygame.draw.circle(screen, "red", _apple_pos, 16)
        
    # Draw snake
    for segment in snake_pos:
        pygame.draw.rect(screen, "#009402", (segment[0], segment[1], cell, cell))

    # Draw score
    score_text = font.render(f"Score: {len(snake_pos) - 3}", True, "white")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(7)

pygame.quit()
