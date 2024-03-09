import pygame
import sys

# Set up pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Contagious Disease Spread Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.Font(None, 40)
SMALL_FONT = pygame.font.Font(None, 30)

# Simulation settings
TIME_STEP = 200  # Number of milliseconds per time step (200ms for slower visualization)
days_left = 30  # Days left within the 30-day period
POPULATION_SIZE = 0
INITIAL_INFECTIONS = 0
infections = 0
capacity = False

#Picture settings
happy_corgi = pygame.image.load("images/happy_corgi.png").convert_alpha()
scared_corgi = pygame.image.load("images/scared_corgi.png").convert_alpha()
cry_corgi = pygame.image.load("images/cry_corgi.png").convert_alpha()
happy_rect = happy_corgi.get_rect(center = (WIDTH/2, HEIGHT/2))
scared_rect = scared_corgi.get_rect(center = (WIDTH/2, HEIGHT/2))
cry_rect = cry_corgi.get_rect(center = (WIDTH/2, HEIGHT/2))

#music
bg_music = pygame.mixer.Sound("music/leap.wav")
bg_music.set_volume(0.3)
bg_music.play(loops = -1)
population_sound = pygame.mixer.Sound("music/bubbles.wav")


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MESIPASS, filename)
    else:
        return filename

# Function to show start screen and get user inputs
def show_start_screen():
    global POPULATION_SIZE, INITIAL_INFECTIONS

    intro = True
    while intro:
        SCREEN.fill(WHITE)
        title_text = FONT.render("Contagious Disease Spread Simulation", True, BLUE)
        SCREEN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        prompt_text = SMALL_FONT.render("Enter Population Size (Press Enter to Proceed):", True, BLACK)
        SCREEN.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2 - 60))

        # Display the population size entered
        pop_size_text = FONT.render(str(POPULATION_SIZE), True, BLACK)
        SCREEN.blit(pop_size_text, (WIDTH // 2 - pop_size_text.get_width() // 2, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

            # Get user inputs for population size
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_BACKSPACE:
                  POPULATION_SIZE = POPULATION_SIZE // 10
              elif event.key == pygame.K_0:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 0
              elif event.key == pygame.K_1:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 1
              elif event.key == pygame.K_2:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 2
              elif event.key == pygame.K_3:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 3
              elif event.key == pygame.K_4:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 4
              elif event.key == pygame.K_5:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 5
              elif event.key == pygame.K_6:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 6
              elif event.key == pygame.K_7:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 7
              elif event.key == pygame.K_8:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 8
              elif event.key == pygame.K_9:
                  POPULATION_SIZE = POPULATION_SIZE * 10 + 9

        pygame.display.update()

    # Reset the screen and set up the initial infections input
    SCREEN.fill(WHITE)
    pygame.display.update()

    intro = True
    while intro:
        SCREEN.fill(WHITE)
        title_text = FONT.render("Contagious Disease Spread Simulation", True, BLUE)
        SCREEN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        prompt_text = SMALL_FONT.render("Enter Initial Infections (Press Enter to Proceed):", True, BLACK)
        SCREEN.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2 - 60))

        # Display the initial infections entered
        initial_infections_text = FONT.render(str(INITIAL_INFECTIONS), True, BLACK)
        SCREEN.blit(initial_infections_text, (WIDTH // 2 - initial_infections_text.get_width() // 2, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

            # Get user inputs for initial infections
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_BACKSPACE:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS // 10
              elif event.key == pygame.K_0:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 0
              elif event.key == pygame.K_1:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 1
              elif event.key == pygame.K_2:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 2
              elif event.key == pygame.K_3:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 3
              elif event.key == pygame.K_4:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 4
              elif event.key == pygame.K_5:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 5
              elif event.key == pygame.K_6:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 6 
              elif event.key == pygame.K_7:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 7
              elif event.key == pygame.K_8:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 8
              elif event.key == pygame.K_9:
                  INITIAL_INFECTIONS = INITIAL_INFECTIONS * 10 + 9

        pygame.display.update()

    # Reset the screen after input is complete
    SCREEN.fill(WHITE)
    pygame.display.update()

#Jenny Nguyen
#update simulation for each timestep
def update_simulation():
    global infections, days_left
    survivor_text = SMALL_FONT.render("You survived the infection!", True, BLACK)
    if days_left == 30:
        infections = INITIAL_INFECTIONS
    if days_left > 0:
        infections *= 2  # Exponential growth (doubles daily)

        # Display a message when infections reach the total population size
        if infections >= POPULATION_SIZE:
            infections = POPULATION_SIZE
            capacity = True
            return capacity

    days_left -= 1

# Function to draw the simulation on the screen
def draw_simulation():
    SCREEN.fill(WHITE)

    # Draw infections count
    infections_text = FONT.render(f"Infections: {infections}", True, BLACK)
    SCREEN.blit(infections_text, (5, 30))

    # Draw countdown indicator
    countdown_text = FONT.render(f"Days Left: {days_left}", True, BLACK)
    SCREEN.blit(countdown_text, (WIDTH - countdown_text.get_width() - 15, 30))

    #population indicator
    population_text = FONT.render(f"Pop: {POPULATION_SIZE}", True, BLACK)
    SCREEN.blit(population_text, (WIDTH / 2 - population_text.get_width() / 2, 30))


    if infections < POPULATION_SIZE / 2:
        SCREEN.blit(happy_corgi, happy_rect)
    elif infections > POPULATION_SIZE / 2 and infections < POPULATION_SIZE:
        SCREEN.blit(scared_corgi, scared_rect)
        population_sound.play()
    elif infections == POPULATION_SIZE:
        SCREEN.blit(cry_corgi,cry_rect)
        capacity = True
        display_capacity_message("Infections reached total population size!")
        pygame.display.flip()
        pygame.event.pump()
        for event in pygame.event.get():
          if event.type != pygame.QUIT:
            pygame.time.delay(4000)
            pygame.quit()
            sys.exit()
          else:
              pygame.quit()
              sys.exit()
        


    pygame.display.update()

def display_capacity_message(message):
    capacity_text = SMALL_FONT.render(message, True, RED)
    SCREEN.blit(capacity_text, (WIDTH // 2 - capacity_text.get_width() // 2, HEIGHT // 2 + 90))

# Main function
def main():
    global infections

    show_start_screen()

    # Set initial infections count
    infections = INITIAL_INFECTIONS

    # Main game loop
    while days_left > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    update_simulation()

        draw_simulation()

        pygame.time.delay(TIME_STEP)

if __name__ == "__main__":
    main()