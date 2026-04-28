import pygame
import math
import random

# Initial Setup
WIDTH, HEIGHT = 800, 800
FPS = 60
CENTER = (WIDTH // 2, HEIGHT // 2)

# Colors
BLACK = (0, 0, 0)
BALL_COLOR = (255, 50, 50)
CIRCLE_COLOR = (50, 150, 255)

# Physics Constants
GRAVITY = 0.2
BOUNCE_STRENGTH = 2.00  # Energy gain/loss (1.0 = perfect bounce)
MIN_CIRCLE_RADIUS = 1
RADIUS_REDUCTION = .001

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shrinking Circle Physics Sim")
    clock = pygame.time.Clock()

    # Initial State
    outer_radius = 350
    ball_pos = [WIDTH // 2, HEIGHT // 2 - 100]
    ball_vel = [5.0, 0.0]
    ball_radius = 15

    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 1. Apply Physics
        ball_vel[1] += GRAVITY
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # 2. Collision Detection
        dx = ball_pos[0] - CENTER[0]
        dy = ball_pos[1] - CENTER[1]
        dist = math.sqrt(dx**2 + dy**2)

        if dist + ball_radius > outer_radius:
            # Calculate Normal vector (pointing inward from impact)
            nx, ny = dx / dist, dy / dist
            
            # Reflect velocity using Vector Math: v = v - 2 * (v.n) * n
            dot = ball_vel[0] * nx + ball_vel[1] * ny
            ball_vel[0] = (ball_vel[0] - 2 * dot * nx) * BOUNCE_STRENGTH
            ball_vel[1] = (ball_vel[1] - 2 * dot * ny) * BOUNCE_STRENGTH
            
            # Prevent "tunneling" by snapping ball back inside the circle
            overlap = (dist + ball_radius) - outer_radius
            ball_pos[0] -= nx * overlap
            ball_pos[1] -= ny * overlap
            
            # Shrink the outer boundary
            if outer_radius > MIN_CIRCLE_RADIUS:
                outer_radius -= RADIUS_REDUCTION

        # 3. Draw Elements
        pygame.draw.circle(screen, CIRCLE_COLOR, CENTER, int(outer_radius), 4)
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
