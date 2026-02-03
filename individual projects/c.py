import pygame
import random
import math
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Explorer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 50)
PURPLE = (180, 50, 230)
BROWN = (150, 100, 50)
GRAY = (100, 100, 100)
DARK_GREEN = (20, 80, 20)
DARK_GRAY = (50, 50, 50)
LIGHT_BLUE = (100, 150, 255)

# Game states
class GameState(Enum):
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3
    VICTORY = 4

# Direction enum for animations
class Direction(Enum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3

class Particle:
    def __init__(self, x, y, color, velocity_x=0, velocity_y=0, lifetime=30):
        self.x = x
        self.y = y
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = random.randint(2, 5)
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_x *= 0.95
        self.velocity_y *= 0.95
        self.lifetime -= 1
        self.size = max(1, int(self.size * (self.lifetime / self.max_lifetime)))
    
    def draw(self, surface, camera_x, camera_y):
        if self.lifetime > 0:
            pygame.draw.circle(surface, self.color, 
                             (int(self.x - camera_x), int(self.y - camera_y)), 
                             self.size)

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
    
    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self, surface, camera_x, camera_y):
        pygame.draw.rect(surface, self.color, 
                        (self.x - camera_x, self.y - camera_y, 
                         self.width, self.height))

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, BLUE)
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.exp = 0
        self.level = 1
        self.exp_to_next_level = 50
        self.attack_power = 10
        self.defense = 2
        self.inventory = []
        self.attack_cooldown = 0
        self.attack_range = 50
        self.direction = Direction.DOWN
        self.animation_frame = 0
        self.animation_timer = 0
        self.invincible_timer = 0
    
    def update(self, keys, enemies, projectiles):
        # Handle invincibility frames
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        
        # Movement
        dx, dy = 0, 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= self.speed
            self.direction = Direction.UP
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed
            self.direction = Direction.DOWN
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= self.speed
            self.direction = Direction.LEFT
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += self.speed
            self.direction = Direction.RIGHT
        
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071
        
        # Update position
        self.x += dx
        self.y += dy
        
        # Keep player in bounds
        self.x = max(0, min(self.x, 2000))
        self.y = max(0, min(self.y, 2000))
        
        # Update animation
        if dx != 0 or dy != 0:
            self.animation_timer += 1
            if self.animation_timer >= 10:
                self.animation_frame = (self.animation_frame + 1) % 4
                self.animation_timer = 0
        
        # Update attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        # Update rectangle
        self.update_rect()
        
        # Check collision with enemies
        for enemy in enemies[:]:
            if self.rect.colliderect(enemy.rect):
                if self.invincible_timer == 0:
                    damage = max(1, enemy.attack_power - self.defense)
                    self.health -= damage
                    self.invincible_timer = 30
                    if self.health <= 0:
                        return False
        
        # Check collision with projectiles
        for projectile in projectiles[:]:
            if self.rect.colliderect(projectile.rect) and projectile.enemy_owned:
                if self.invincible_timer == 0:
                    self.health -= projectile.damage
                    self.invincible_timer = 30
                    projectiles.remove(projectile)
                    if self.health <= 0:
                        return False
        
        return True
    
    def attack(self, enemies, particles):
        if self.attack_cooldown == 0:
            self.attack_cooldown = 20
            
            # Determine attack position based on direction
            attack_x, attack_y = self.x, self.y
            if self.direction == Direction.UP:
                attack_y -= 40
            elif self.direction == Direction.DOWN:
                attack_y += 40
            elif self.direction == Direction.LEFT:
                attack_x -= 40
            elif self.direction == Direction.RIGHT:
                attack_x += 40
            
            # Create attack particles
            for _ in range(10):
                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(1, 3)
                particles.append(Particle(
                    attack_x + 16, attack_y + 16,
                    LIGHT_BLUE,
                    math.cos(angle) * speed,
                    math.sin(angle) * speed,
                    random.randint(10, 20)
                ))
            
            # Check for hit enemies
            for enemy in enemies[:]:
                distance = math.sqrt((enemy.x - attack_x)**2 + (enemy.y - attack_y)**2)
                if distance < self.attack_range:
                    enemy.take_damage(self.attack_power, particles)
                    if enemy.health <= 0:
                        self.exp += enemy.exp_value
                        enemies.remove(enemy)
            
            return True
        return False
    
    def draw(self, surface, camera_x, camera_y):
        # Draw player with animation
        player_color = self.color
        if self.invincible_timer > 0 and self.invincible_timer % 4 < 2:
            player_color = WHITE
        
        # Draw player body
        pygame.draw.rect(surface, player_color, 
                        (self.x - camera_x, self.y - camera_y, 
                         self.width, self.height))
        
        # Draw direction indicator
        indicator_x, indicator_y = self.x + 16, self.y + 16
        if self.direction == Direction.UP:
            indicator_y -= 20
        elif self.direction == Direction.DOWN:
            indicator_y += 20
        elif self.direction == Direction.LEFT:
            indicator_x -= 20
        elif self.direction == Direction.RIGHT:
            indicator_x += 20
        
        pygame.draw.circle(surface, YELLOW, 
                          (int(indicator_x - camera_x), int(indicator_y - camera_y)), 8)
    
    def check_level_up(self):
        if self.exp >= self.exp_to_next_level:
            self.level += 1
            self.exp -= self.exp_to_next_level
            self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
            self.max_health += 20
            self.health = self.max_health
            self.attack_power += 5
            self.defense += 1
            return True
        return False
    
    def add_item(self, item):
        if len(self.inventory) < 10:
            self.inventory.append(item)
            return True
        return False

class Enemy(GameObject):
    def __init__(self, x, y, enemy_type="goblin"):
        super().__init__(x, y, 32, 32, RED)
        self.enemy_type = enemy_type
        self.speed = random.uniform(1.0, 2.0)
        self.health = 30
        self.max_health = 30
        self.attack_power = 5
        self.exp_value = 10
        self.attack_cooldown = 0
        self.color = RED if enemy_type == "goblin" else PURPLE
        self.patrol_timer = random.randint(0, 100)
        self.patrol_direction = random.uniform(0, math.pi * 2)
        
        if enemy_type == "archer":
            self.health = 20
            self.max_health = 20
            self.speed = 1.5
            self.attack_range = 150
            self.attack_power = 8
            self.color = GREEN
            self.exp_value = 15
        elif enemy_type == "tank":
            self.health = 80
            self.max_health = 80
            self.speed = 0.8
            self.attack_power = 15
            self.color = BROWN
            self.exp_value = 25
    
    def update(self, player, projectiles):
        # Update attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        # Calculate distance to player
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Enemy behavior based on type
        if self.enemy_type == "goblin":
            # Chase player if close
            if distance < 200:
                if distance > 30:  # Don't get too close
                    dx /= distance
                    dy /= distance
                    self.x += dx * self.speed
                    self.y += dy * self.speed
            else:
                # Patrol randomly
                self.patrol_timer -= 1
                if self.patrol_timer <= 0:
                    self.patrol_timer = random.randint(30, 120)
                    self.patrol_direction = random.uniform(0, math.pi * 2)
                
                self.x += math.cos(self.patrol_direction) * self.speed * 0.5
                self.y += math.sin(self.patrol_direction) * self.speed * 0.5
        
        elif self.enemy_type == "archer":
            # Keep distance and shoot
            if distance < self.attack_range:
                if distance < 100:  # Too close, back away
                    self.x -= dx / distance * self.speed
                    self.y -= dy / distance * self.speed
                
                # Shoot at player
                if self.attack_cooldown == 0 and distance < self.attack_range:
                    self.shoot(dx, dy, distance, projectiles)
                    self.attack_cooldown = 60
            else:
                # Chase player
                if distance > 0:
                    self.x += dx / distance * self.speed
                    self.y += dy / distance * self.speed
        
        elif self.enemy_type == "tank":
            # Slow but relentless chase
            if distance > 0:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed
        
        # Keep enemy in bounds
        self.x = max(0, min(self.x, 2000))
        self.y = max(0, min(self.y, 2000))
        
        # Update rectangle
        self.update_rect()
    
    def shoot(self, dx, dy, distance, projectiles):
        if distance > 0:
            projectile_speed = 5
            projectiles.append(Projectile(
                self.x + 16, self.y + 16,
                dx / distance * projectile_speed,
                dy / distance * projectile_speed,
                GREEN, 8, enemy_owned=True, damage=8
            ))
    
    def take_damage(self, damage, particles):
        self.health -= damage
        
        # Create damage particles
        for _ in range(5):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(1, 3)
            particles.append(Particle(
                self.x + 16, self.y + 16,
                YELLOW,
                math.cos(angle) * speed,
                math.sin(angle) * speed,
                random.randint(10, 20)
            ))
    
    def draw(self, surface, camera_x, camera_y):
        # Draw enemy
        pygame.draw.rect(surface, self.color, 
                        (self.x - camera_x, self.y - camera_y, 
                         self.width, self.height))
        
        # Draw health bar
        bar_width = 32
        bar_height = 5
        health_ratio = self.health / self.max_health
        pygame.draw.rect(surface, RED, 
                        (self.x - camera_x, self.y - camera_y - 10, 
                         bar_width, bar_height))
        pygame.draw.rect(surface, GREEN, 
                        (self.x - camera_x, self.y - camera_y - 10, 
                         bar_width * health_ratio, bar_height))

class Projectile(GameObject):
    def __init__(self, x, y, velocity_x, velocity_y, color, size, enemy_owned=False, damage=10):
        super().__init__(x, y, size, size, color)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.enemy_owned = enemy_owned
        self.damage = damage
        self.lifetime = 180  # Projectiles disappear after 3 seconds at 60 FPS
    
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.lifetime -= 1
        self.update_rect()
        
        # Remove if out of bounds or lifetime expired
        if (self.x < 0 or self.x > 2000 or 
            self.y < 0 or self.y > 2000 or 
            self.lifetime <= 0):
            return False
        return True
    
    def draw(self, surface, camera_x, camera_y):
        pygame.draw.circle(surface, self.color, 
                          (int(self.x - camera_x), int(self.y - camera_y)), 
                          self.width // 2)

class Item(GameObject):
    def __init__(self, x, y, item_type="health"):
        super().__init__(x, y, 20, 20, RED)
        self.item_type = item_type
        
        if item_type == "health":
            self.color = RED
        elif item_type == "exp":
            self.color = YELLOW
        elif item_type == "speed":
            self.color = BLUE
        elif item_type == "power":
            self.color = PURPLE
    
    def apply_effect(self, player):
        if self.item_type == "health":
            player.health = min(player.max_health, player.health + 30)
            return "Health +30!"
        elif self.item_type == "exp":
            player.exp += 25
            return "EXP +25!"
        elif self.item_type == "speed":
            player.speed += 1
            return "Speed Increased!"
        elif self.item_type == "power":
            player.attack_power += 3
            return "Attack Power +3!"
        return ""

class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_size = 64
        self.rooms = []
        self.corridors = []
        self.generate_dungeon()
    
    def generate_dungeon(self):
        # Generate rooms
        num_rooms = random.randint(8, 12)
        for _ in range(num_rooms):
            room_width = random.randint(5, 10) * self.tile_size
            room_height = random.randint(5, 8) * self.tile_size
            room_x = random.randint(0, (self.width - room_width) // self.tile_size) * self.tile_size
            room_y = random.randint(0, (self.height - room_height) // self.tile_size) * self.tile_size
            
            # Make sure rooms don't overlap too much
            overlap = False
            for existing_room in self.rooms:
                if (abs(room_x - existing_room[0]) < room_width + self.tile_size * 2 and
                    abs(room_y - existing_room[1]) < room_height + self.tile_size * 2):
                    overlap = True
                    break
            
            if not overlap:
                self.rooms.append((room_x, room_y, room_width, room_height))
        
        # Connect rooms with corridors
        for i in range(len(self.rooms) - 1):
            room1 = self.rooms[i]
            room2 = self.rooms[i + 1]
            
            # Center points of rooms
            x1, y1 = room1[0] + room1[2] // 2, room1[1] + room1[3] // 2
            x2, y2 = room2[0] + room2[2] // 2, room2[1] + room2[3] // 2
            
            # Create L-shaped corridor
            if random.choice([True, False]):
                # Horizontal then vertical
                self.corridors.append((min(x1, x2), y1, abs(x1 - x2), self.tile_size))
                self.corridors.append((x2, min(y1, y2), self.tile_size, abs(y1 - y2)))
            else:
                # Vertical then horizontal
                self.corridors.append((x1, min(y1, y2), self.tile_size, abs(y1 - y2)))
                self.corridors.append((min(x1, x2), y2, abs(x1 - x2), self.tile_size))
    
    def draw(self, surface, camera_x, camera_y):
        # Draw corridors
        for corridor in self.corridors:
            pygame.draw.rect(surface, DARK_GRAY, 
                           (corridor[0] - camera_x, corridor[1] - camera_y, 
                            corridor[2], corridor[3]))
        
        # Draw rooms
        for room in self.rooms:
            pygame.draw.rect(surface, GRAY, 
                           (room[0] - camera_x, room[1] - camera_y, 
                            room[2], room[3]))
            
            # Draw room border
            pygame.draw.rect(surface, DARK_GRAY, 
                           (room[0] - camera_x, room[1] - camera_y, 
                            room[2], room[3]), 3)
        
        # Draw grid lines
        for x in range(0, self.width, self.tile_size):
            pygame.draw.line(surface, DARK_GRAY, 
                           (x - camera_x, 0), 
                           (x - camera_x, self.height), 1)
        for y in range(0, self.height, self.tile_size):
            pygame.draw.line(surface, DARK_GRAY, 
                           (0, y - camera_y), 
                           (self.width, y - camera_y), 1)

class Game:
    def __init__(self):
        self.state = GameState.PLAYING
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.particles = []
        self.projectiles = []
        self.enemies = []
        self.items = []
        self.enemy_spawn_timer = 0
        self.item_spawn_timer = 0
        self.wave = 1
        self.enemies_killed = 0
        self.enemies_to_next_wave = 10
        self.boss_spawned = False
        
        # Create dungeon
        self.dungeon = Dungeon(2000, 2000)
        
        # Create player at center of first room
        first_room = self.dungeon.rooms[0]
        player_x = first_room[0] + first_room[2] // 2
        player_y = first_room[1] + first_room[3] // 2
        self.player = Player(player_x, player_y)
        
        # Spawn initial enemies
        self.spawn_initial_enemies()
        
        # Camera
        self.camera_x = 0
        self.camera_y = 0
    
    def spawn_initial_enemies(self):
        for room in self.dungeon.rooms[1:3]:  # Spawn in first few rooms
            for _ in range(random.randint(2, 4)):
                enemy_x = room[0] + random.randint(0, room[2] - 32)
                enemy_y = room[1] + random.randint(0, room[3] - 32)
                enemy_type = random.choice(["goblin", "goblin", "archer"])
                self.enemies.append(Enemy(enemy_x, enemy_y, enemy_type))
    
    def spawn_enemy(self):
        # Spawn enemy in a random room (not the player's current room)
        if len(self.dungeon.rooms) > 1:
            room = random.choice(self.dungeon.rooms[1:])
            enemy_x = room[0] + random.randint(0, room[2] - 32)
            enemy_y = room[1] + random.randint(0, room[3] - 32)
            
            # Determine enemy type based on wave
            enemy_types = ["goblin"] * 5 + ["archer"] * 3
            if self.wave >= 3:
                enemy_types += ["tank"] * 2
            
            enemy_type = random.choice(enemy_types)
            self.enemies.append(Enemy(enemy_x, enemy_y, enemy_type))
    
    def spawn_item(self):
        if len(self.items) < 5:  # Max 5 items at once
            room = random.choice(self.dungeon.rooms)
            item_x = room[0] + random.randint(0, room[2] - 20)
            item_y = room[1] + random.randint(0, room[3] - 20)
            item_type = random.choice(["health", "exp", "speed", "power"])
            self.items.append(Item(item_x, item_y, item_type))
    
    def update_camera(self):
        # Center camera on player
        self.camera_x = self.player.x - SCREEN_WIDTH // 2
        self.camera_y = self.player.y - SCREEN_HEIGHT // 2
        
        # Keep camera within dungeon bounds
        self.camera_x = max(0, min(self.camera_x, self.dungeon.width - SCREEN_WIDTH))
        self.camera_y = max(0, min(self.camera_y, self.dungeon.height - SCREEN_HEIGHT))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.PLAYING
                
                if event.key == pygame.K_SPACE:
                    if self.state == GameState.PLAYING:
                        self.player.attack(self.enemies, self.particles)
                
                if event.key == pygame.K_r:
                    if self.state in [GameState.GAME_OVER, GameState.VICTORY]:
                        self.__init__()  # Restart game
                
                if event.key == pygame.K_e:
                    # Pick up nearby items
                    for item in self.items[:]:
                        distance = math.sqrt((item.x - self.player.x)**2 + (item.y - self.player.y)**2)
                        if distance < 50:
                            message = item.apply_effect(self.player)
                            self.items.remove(item)
                            
                            # Show pickup message
                            self.particles.append(Particle(
                                self.player.x, self.player.y - 30,
                                WHITE, 0, -1, 60
                            ))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if self.state == GameState.PLAYING:
                        self.player.attack(self.enemies, self.particles)
        
        return True
    
    def update(self):
        if self.state != GameState.PLAYING:
            return
        
        keys = pygame.key.get_pressed()
        
        # Update player
        if not self.player.update(keys, self.enemies, self.projectiles):
            self.state = GameState.GAME_OVER
            return
        
        # Check level up
        if self.player.check_level_up():
            # Create level up particles
            for _ in range(30):
                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(2, 5)
                self.particles.append(Particle(
                    self.player.x + 16, self.player.y + 16,
                    YELLOW,
                    math.cos(angle) * speed,
                    math.sin(angle) * speed,
                    random.randint(20, 40)
                ))
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update(self.player, self.projectiles)
        
        # Update projectiles
        for projectile in self.projectiles[:]:
            if not projectile.update():
                self.projectiles.remove(projectile)
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.lifetime <= 0:
                self.particles.remove(particle)
        
        # Spawn enemies periodically
        self.enemy_spawn_timer += 1
        if self.enemy_spawn_timer >= 180 and len(self.enemies) < 15:  # Spawn every 3 seconds
            self.spawn_enemy()
            self.enemy_spawn_timer = 0
        
        # Spawn items periodically
        self.item_spawn_timer += 1
        if self.item_spawn_timer >= 300:  # Spawn every 5 seconds
            self.spawn_item()
            self.item_spawn_timer = 0
        
        # Check for wave progression
        if self.enemies_killed >= self.enemies_to_next_wave:
            self.wave += 1
            self.enemies_killed = 0
            self.enemies_to_next_wave += 5
            
            # Spawn wave enemies
            for _ in range(min(self.wave * 3, 15)):
                self.spawn_enemy()
            
            # Spawn boss on wave 5
            if self.wave >= 5 and not self.boss_spawned:
                self.spawn_boss()
                self.boss_spawned = True
        
        # Update camera
        self.update_camera()
        
        # Check win condition
        if self.wave >= 10:
            self.state = GameState.VICTORY
    
    def spawn_boss(self):
        room = random.choice(self.dungeon.rooms)
        boss_x = room[0] + room[2] // 2
        boss_y = room[1] + room[3] // 2
        boss = Enemy(boss_x, boss_y, "tank")
        boss.health = 200
        boss.max_health = 200
        boss.attack_power = 25
        boss.exp_value = 100
        boss.color = PURPLE
        boss.width = 64
        boss.height = 64
        self.enemies.append(boss)
    
    def draw(self):
        # Clear screen
        screen.fill(BLACK)
        
        # Draw dungeon
        self.dungeon.draw(screen, self.camera_x, self.camera_y)
        
        # Draw items
        for item in self.items:
            item.draw(screen, self.camera_x, self.camera_y)
        
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(screen, self.camera_x, self.camera_y)
        
        # Draw projectiles
        for projectile in self.projectiles:
            projectile.draw(screen, self.camera_x, self.camera_y)
        
        # Draw particles
        for particle in self.particles:
            particle.draw(screen, self.camera_x, self.camera_y)
        
        # Draw player
        self.player.draw(screen, self.camera_x, self.camera_y)
        
        # Draw UI
        self.draw_ui()
        
        # Draw game state screens
        if self.state == GameState.PAUSED:
            self.draw_pause_screen()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over_screen()
        elif self.state == GameState.VICTORY:
            self.draw_victory_screen()
        
        # Update display
        pygame.display.flip()
    
    def draw_ui(self):
        # Health bar
        health_ratio = self.player.health / self.player.max_health
        bar_width = 200
        bar_height = 25
        
        # Background
        pygame.draw.rect(screen, DARK_GRAY, (10, 10, bar_width, bar_height))
        # Health fill
        pygame.draw.rect(screen, RED, (10, 10, bar_width * health_ratio, bar_height))
        # Border
        pygame.draw.rect(screen, WHITE, (10, 10, bar_width, bar_height), 2)
        
        # Health text
        health_text = self.font.render(f"HP: {int(self.player.health)}/{self.player.max_health}", True, WHITE)
        screen.blit(health_text, (15, 12))
        
        # EXP bar
        exp_ratio = self.player.exp / self.player.exp_to_next_level
        exp_bar_width = 200
        exp_bar_height = 15
        
        pygame.draw.rect(screen, DARK_GRAY, (10, 45, exp_bar_width, exp_bar_height))
        pygame.draw.rect(screen, YELLOW, (10, 45, exp_bar_width * exp_ratio, exp_bar_height))
        pygame.draw.rect(screen, WHITE, (10, 45, exp_bar_width, exp_bar_height), 2)
        
        # EXP text
        exp_text = self.small_font.render(f"EXP: {self.player.exp}/{self.player.exp_to_next_level}", True, WHITE)
        screen.blit(exp_text, (15, 47))
        
        # Level
        level_text = self.font.render(f"Level: {self.player.level}", True, WHITE)
        screen.blit(level_text, (SCREEN_WIDTH - 150, 10))
        
        # Wave
        wave_text = self.font.render(f"Wave: {self.wave}", True, WHITE)
        screen.blit(wave_text, (SCREEN_WIDTH - 150, 50))
        
        # Stats
        stats_y = 100
        stats = [
            f"Attack: {self.player.attack_power}",
            f"Defense: {self.player.defense}",
            f"Speed: {self.player.speed}",
            f"Enemies Killed: {self.enemies_killed}"
        ]
        
        for i, stat in enumerate(stats):
            stat_text = self.small_font.render(stat, True, WHITE)
            screen.blit(stat_text, (10, stats_y + i * 25))
        
        # Inventory
        inv_text = self.small_font.render(f"Inventory: {len(self.player.inventory)}/10", True, WHITE)
        screen.blit(inv_text, (10, SCREEN_HEIGHT - 30))
        
        # Controls help
        controls = [
            "WASD/Arrows: Move",
            "Space/Mouse: Attack",
            "E: Pick up items",
            "ESC: Pause"
        ]
        
        for i, control in enumerate(controls):
            control_text = self.small_font.render(control, True, GRAY)
            screen.blit(control_text, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 100 + i * 25))
    
    def draw_pause_screen(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render("PAUSED", True, WHITE)
        continue_text = self.small_font.render("Press ESC to continue", True, WHITE)
        
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
    
    def draw_game_over_screen(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((50, 0, 0, 200))
        screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER", True, RED)
        stats_text = self.small_font.render(f"Wave Reached: {self.wave}  Level: {self.player.level}", True, WHITE)
        restart_text = self.small_font.render("Press R to restart", True, WHITE)
        
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(stats_text, (SCREEN_WIDTH // 2 - stats_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    
    def draw_victory_screen(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 50, 0, 200))
        screen.blit(overlay, (0, 0))
        
        victory_text = self.font.render("VICTORY!", True, GREEN)
        stats_text = self.small_font.render(f"You cleared all waves! Final Level: {self.player.level}", True, WHITE)
        restart_text = self.small_font.render("Press R to play again", True, WHITE)
        
        screen.blit(victory_text, (SCREEN_WIDTH // 2 - victory_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(stats_text, (SCREEN_WIDTH // 2 - stats_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()