import pygame
import random

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
GREEN = (0, 255, 0)

# Fuente para el puntaje y mensajes
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

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

# Clase para los enemigos
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 3
    
    def move(self):
        self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

# Función para mostrar el menú

def show_menu():
    while True:
        screen.fill(BLACK)
        title_text = large_font.render("Shooter 2D", True, WHITE)
        start_text = font.render("Presiona ENTER para comenzar", True, WHITE)
        exit_text = font.render("Presiona ESC para salir", True, WHITE)
        
        screen.blit(title_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(start_text, (WIDTH // 2 - 150, HEIGHT // 2))
        screen.blit(exit_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Iniciar el juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Función principal del juego
def main():
    show_menu()
    
    while True:
        running = True
        player = Player(WIDTH // 2, HEIGHT - 60)
        bullets = []
        enemies = []
        spawn_timer = 0
        score = 0
        game_over = False
        
        while running:
            screen.fill(BLACK)  # Limpiar pantalla
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not game_over:
                        bullets.append(Bullet(player.rect.x, player.rect.y))
                    elif event.key == pygame.K_r and game_over:
                        return  # Reiniciar el juego
            
            if not game_over:
                keys = pygame.key.get_pressed()
                player.move(keys)
                
                for bullet in bullets[:]:
                    bullet.move()
                    if bullet.rect.y < 0:
                        bullets.remove(bullet)
                
                if spawn_timer <= 0:
                    enemies.append(Enemy(random.randint(0, WIDTH - 50), 0))
                    spawn_timer = 60  # Genera un enemigo cada segundo
                spawn_timer -= 1
                
                for enemy in enemies[:]:
                    enemy.move()
                    if enemy.rect.y > HEIGHT:
                        game_over = True
                    
                # Detección de colisiones
                for bullet in bullets[:]:
                    for enemy in enemies[:]:
                        if bullet.rect.colliderect(enemy.rect):
                            bullets.remove(bullet)
                            enemies.remove(enemy)
                            score += 10
                            break
            
            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            
            # Dibujar el puntaje
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            # Mostrar pantalla de Game Over con opción de reinicio
            if game_over:
                game_over_text = large_font.render("GAME OVER", True, RED)
                restart_text = font.render("Presiona 'R' para reiniciar", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
                screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 20))
            
            pygame.display.flip()  # Actualizar pantalla
            clock.tick(60)  # Limitar a 60 FPS

if __name__ == "__main__":
    main()
