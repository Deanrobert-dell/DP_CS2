import pygame
import math
import random

# Initial Setup
WIDTH, HEIGHT = 800, 800
FPS = 60
CENTER = (WIDTH // 2, HEIGHT // 2)

# Colors
BLACK = (0, 0, 0)

# Physics Constants
GRAVITY = 100
BOUNCE_STRENGTH = 1.00
MIN_CIRCLE_RADIUS = -100
RADIUS_REDUCTION_ON_BOUNCE = 1.0000001  # Slower shrink happening only on bounce

class Ball:
    def __init__(self, x, y, vx, vy, radius=15):
        self.pos = [x, y]
        self.vel = [vx, vy]
        self.radius = radius
        # Give each ball its own random color
        self.color = [random.randint(50, 255) for _ in range(3)]
        self.trail = []
        self.max_trail_length = 20

    def update_physics(self):
        self.vel[1] += GRAVITY
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def update_trail(self):
        speed = math.sqrt(self.vel[0]**2 + self.vel[1]**2)
        # Keeps trail thickness way smaller than the ball's radius
        trail_thickness = max(2.0, min(self.radius * 0.6, speed * 0.8))
        self.trail.append((self.pos[0], self.pos[1], trail_thickness))
        
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

    def draw(self, screen):
        # 1. Draw dynamic fading trail
        for i, (tx, ty, t_thick) in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            trail_surface = pygame.Surface((t_thick * 2, t_thick * 2), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, (*self.color, alpha), (int(t_thick), int(t_thick)), int(t_thick))
            screen.blit(trail_surface, (int(tx - t_thick), int(ty - t_thick)))

        # 2. Draw active ball
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Multi-Ball Shrinking Circle Sim")
    clock = pygame.time.Clock()

    # Initial State
    outer_radius = 350
    circle_color = [50, 150, 255]
    
    # Store all active balls in a list
    balls = [Ball(WIDTH // 2, HEIGHT // 2 - 100, 5.0, 0.0)]
    
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        new_balls = []

        for ball in balls:
            ball.update_physics()
            ball.update_trail()

            # Collision Detection
            dx = ball.pos[0] - CENTER[0]
            dy = ball.pos[1] - CENTER[1]
            dist = math.sqrt(dx**2 + dy**2)

            if dist + ball.radius > outer_radius:
                nx, ny = dx / dist, dy / dist
                
                # Reflect velocity using vector math
                dot = ball.vel[0] * nx + ball.vel[1] * ny
                ball.vel[0] = (ball.vel[0] - 2 * dot * nx) * BOUNCE_STRENGTH
                ball_vel_y_new = (ball.vel[1] - 2 * dot * ny) * BOUNCE_STRENGTH

                # Snap ball back inside circle
                overlap = (dist + ball.radius) - outer_radius
                ball.pos[0] -= nx * overlap
                ball.pos[1] -= ny * overlap

                # Update current ball's bounce parameters
                ball.vel[1] = ball_vel_y_new
                ball.color = [random.randint(50, 255) for _ in range(3)]
                circle_color = [random.randint(50, 255) for _ in range(3)]

                # Slowly shrink circle size on bounce
                if outer_radius > MIN_CIRCLE_RADIUS:
                    outer_radius -= RADIUS_REDUCTION_ON_BOUNCE

                # Spawn a new ball on bounce
                if len(balls) + len(new_balls) < 50:  # Prevent performance lag
                    # Slight variation in velocity so they don't overlap perfectly
                    vx = ball.vel[0] + random.uniform(-1.5, 1.5)
                    vy = ball.vel[1] + random.uniform(-1.5, 1.5)
                    new_balls.append(Ball(ball.pos[0], ball.pos[1], vx, vy))

        # Add newly spawned balls to main simulation list
        balls.extend(new_balls)

        # Draw the boundary circle (solid, changes color on impact)
        pygame.draw.circle(screen, circle_color, CENTER, int(max(1, outer_radius)), 4)

        # Draw all existing balls and their trails
        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
