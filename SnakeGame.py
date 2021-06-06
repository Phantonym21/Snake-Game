import pygame

import random

pygame.init()

# Generic Variables


# Game Variables
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
# Game Window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
GameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# TITLE
pygame.display.set_caption("Snake")

pygame.display.update()


# MAIN FUNCTION
def game_loop():
    # Generic Variables
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    GameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    snakex = 50  # random.randint(0,SCREEN_WIDTH/2)
    snakey = 50  # random.randint(0,SCREEN_HEIGHT/2)
    snake_size = 10
    snake_move_distance = 5
    snake_Vx = 0
    snake_Vy = 0
    food_x = random.randint(20, SCREEN_WIDTH / 2)
    food_y = random.randint(20, (SCREEN_HEIGHT / 2)-60)
    fps = 30
    score = 0
    font = pygame.font.SysFont(None, 55)

    exit_game = False
    game_over = False

    snake_length = 1
    snake_list = []

    def display_text(text, color, x, y):
        screen_text = font.render(text, True, color)
        GameWindow.blit(screen_text, [x, y])

    def plot_snake(GameWindow, color, snake_list, snake_size):
        for x, y in snake_list:
            pygame.draw.rect(GameWindow, color, [x, y, snake_size, snake_size])

    # MAIN CODE

    while not exit_game:
        if game_over:
            GameWindow.fill(white)
            display_text("Game over press enter to continue", red, 200, 200)
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    exit_game = True
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        game_loop();
        else:
            # For Checking Events
            for e in pygame.event.get():

                if e.type == pygame.QUIT:
                    exit_game = True
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                        snake_Vx = snake_move_distance
                        snake_Vy = 0
                    if e.key == pygame.K_LEFT:
                        snake_Vx = -snake_move_distance
                        snake_Vy = 0
                    if e.key == pygame.K_UP:
                        snake_Vy = -snake_move_distance
                        snake_Vx = 0
                    if e.key == pygame.K_DOWN:
                        snake_Vy = snake_move_distance
                        snake_Vx = 0
            # For Changing Direction
            snakex += snake_Vx
            snakey += snake_Vy

            # Eating Food
            if abs(snakex - food_x) < 8 and abs(snakey - food_y) < 8:
                score += 1
                snake_length += 3
                food_x = random.randint(10, SCREEN_WIDTH / 2)
                food_y = random.randint(10, (SCREEN_HEIGHT / 2) - 60)
                print(score * 10)

            head = []
            head.append(snakex)
            head.append(snakey)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            # Displaying stuff

            GameWindow.fill(white)
            if snakex >= SCREEN_WIDTH or snakex <= 0 or snakey >= SCREEN_HEIGHT or snakey <= 42:
                game_over = True
            if head in snake_list[:-1]:
                game_over = True

            plot_snake(GameWindow, black, snake_list, snake_size)
            pygame.draw.line(GameWindow, black, (0, 42), (SCREEN_WIDTH, 42))
            pygame.draw.rect(GameWindow, red, [food_x, food_y, snake_size, snake_size])
            # pygame.draw.arc(GameWindow, black, [100, 200, 100, 100], math.pi, math.pi/9)
            display_text("Score: " + str(score * 10), yellow, 10, 10)

        pygame.display.update()

        # Tickrate for function
        clock.tick(fps)
    pygame.quit()
    quit()


game_loop()
