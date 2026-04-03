import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# Colors
WHITE = (255,255,255)
GREEN = (0,200,0)

def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x,y))

def main_menu():
    running = True
    while running:
        screen.fill(GREEN)
        draw_text("🏏 Cricket Clans", 500, 200)
        draw_text("Press SPACE to Kick Off", 450, 400)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        
        pygame.display.flip()
        clock.tick(120)

def toss():
    screen.fill((0,0,100))
    draw_text("Heads or Tails? Press H or T", 400, 300)
    pygame.display.flip()
    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h: choice = "heads"
                elif event.key == pygame.K_t: choice = "tails"
    coin = random.choice(["heads","tails"])
    result = "You won the toss!" if choice == coin else "Computer won the toss!"
    screen.fill((0,0,100))
    draw_text(result, 500, 350)
    pygame.display.flip()
    pygame.time.wait(2000)

def game_loop():
    # Placeholder for batting/bowling animations
    screen.fill((50,50,50))
    draw_text("Gameplay goes here...", 500, 300)
    pygame.display.flip()
    pygame.time.wait(3000)

def main():
    main_menu()
    toss()
    game_loop()

if __name__ == "__main__":
    main()
