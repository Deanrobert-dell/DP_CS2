import pygame
import random
import sys

# Setup
pygame.init()
WIN_SIZE = 1000  
GRID_SIZE = 500  
CELL_SIZE = WIN_SIZE // GRID_SIZE 
SCREEN = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("Exponential Neon Snake Swarm")
FONT = pygame.font.Font(None, 36)
SPEED_FONT = pygame.font.Font(None, 50)
CLOCK = pygame.time.Clock()

# Neon Palette
COLORS = [
    (0, 255, 255),   # Cyan
    (255, 0, 255),   # Magenta
    (0, 255, 0),     # Neon Green
    (255, 255, 0),   # Neon Yellow
    (255, 100, 0),   # Neon Orange
    (100, 100, 255), # Neon Blue
    (255, 50, 150),  # Hot Pink
    (0, 255, 150),   # Seafoam
    (200, 255, 0),   # Lime
    (255, 255, 255)  # White
]

def get_mode():
    while True:
        SCREEN.fill((10, 10, 10))
        options = ["1: Human", "2: 1 Bot", "3: 2 Bots", "4: 3 Bots", "5: 4 Bots", "6: 10 BOTS!"]
        title = SPEED_FONT.render("SELECT MODE", True, (255, 255, 255))
        SCREEN.blit(title, (WIN_SIZE//2 - title.get_width()//2, 100))
        for i, text in enumerate(options):
            txt = FONT.render(text, True, (255, 255, 255))
            SCREEN.blit(txt, (WIN_SIZE//2 - txt.get_width()//2, 200 + i*60))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: return 1, False
                if event.key == pygame.K_2: return 1, True
                if event.key == pygame.K_3: return 2, True
                if event.key == pygame.K_4: return 3, True
                if event.key == pygame.K_5: return 4, True
                if event.key == pygame.K_6: return 10, True

def spawn_apple_near(old_pos):
    ox, oy = old_pos
    dist = 100 
    nx = max(0, min(GRID_SIZE - 1, random.randint(ox - dist, ox + dist)))
    ny = max(0, min(GRID_SIZE - 1, random.randint(oy - dist, oy + dist)))
    return (nx, ny)

def bot_logic(head, target):
    hx, hy = head
    tx, ty = target
    if hx < tx: return (1, 0)
    elif hx > tx: return (-1, 0)
    elif hy < ty: return (0, 1)
    elif hy > ty: return (0, -1)
    return (0, 0)

def main():
    num_snakes, is_bot = get_mode()
    
    # Initialize Snakes, Directions, and Apples
    snakes = [[(random.randint(0, 499), random.randint(0, 499))] for _ in range(num_snakes)]
    dirs = [(1, 0) for _ in range(num_snakes)]
    apples = [(random.randint(0, 499), random.randint(0, 499)) for _ in range(num_snakes)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN and not is_bot:
                if event.key == pygame.K_UP and dirs[0] != (0, 1): dirs[0] = (0, -1)
                elif event.key == pygame.K_DOWN and dirs[0] != (0, -1): dirs[0] = (0, 1)
                elif event.key == pygame.K_LEFT and dirs[0] != (1, 0): dirs[0] = (-1, 0)
                elif event.key == pygame.K_RIGHT and dirs[0] != (-1, 0): dirs[0] = (1, 0)

        SCREEN.fill((5, 5, 5)) 

        total_len = 0
        for i in range(num_snakes):
            if is_bot:
                dirs[i] = bot_logic(snakes[i][0], apples[i])
            
            # Movement
            head = snakes[i][0]
            new_head = ((head[0] + dirs[i][0]) % GRID_SIZE, (head[1] + dirs[i][1]) % GRID_SIZE)
            
            # Human death check (Bots are unkillable)
            if not is_bot and new_head in snakes[i]: return main()

            snakes[i].insert(0, new_head)
            
            # Eating Logic
            if new_head == apples[i]:
                apples[i] = spawn_apple_near(apples[i])
            else:
                snakes[i].pop()
            
            total_len += len(snakes[i])

            # Draw Apple
            pygame.draw.rect(SCREEN, (255, 50, 50), (apples[i][0]*CELL_SIZE, apples[i][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            # Draw Snake
            color = COLORS[i % len(COLORS)]
            for segment in snakes[i]:
                pygame.draw.rect(SCREEN, color, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # --- EXPONENTIAL SPEED CALCULATION ---
        base_speed = 150
        growth_rate = 2  # Increases by 1% per segment
        current_score = total_len - num_snakes
        # The exponential formula: speed = base * (1.01 ^ score)
        calculated_speed = int(base_speed * (growth_rate ** current_score))
        
        # We cap it at 10,000 so the computer doesn't catch fire
        final_speed = min(calculated_speed, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        # Draw HUD (Score and Speedometer)
        speed_txt = SPEED_FONT.render(f"SPEED: {final_speed} FPS", True, (255, 255, 255))
        score_txt = FONT.render(f"TOTAL SEGMENTS: {total_len}", True, (255, 255, 255))
        SCREEN.blit(speed_txt, (20, 20))
        SCREEN.blit(score_txt, (20, 70))

        pygame.display.flip()
        
        # Apply the exponential tick
        CLOCK.tick(final_speed if is_bot else 60)

if __name__ == "__main__":
    main()
