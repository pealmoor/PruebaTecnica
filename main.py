import pygame

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter 2D")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Clase para el jugador
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 5
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

# Clase para los disparos
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x + 20, y, 10, 20)
        self.speed = -7
    
    def move(self):
        self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

# Bucle principal
def main():
    running = True
    player = Player(WIDTH // 2, HEIGHT - 60)
    bullets = []
    
    while running:
        screen.fill(BLACK)  # Limpiar pantalla
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.rect.x, player.rect.y))
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.y < 0:
                bullets.remove(bullet)
        
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
        pygame.display.flip()  # Actualizar pantalla
        clock.tick(60)  # Limitar a 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
