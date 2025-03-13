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

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal
def main():
    running = True
    while running:
        screen.fill(BLACK)  # Limpiar pantalla
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()  # Actualizar pantalla
        clock.tick(60)  # Limitar a 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()

