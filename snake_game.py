import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600

# Colours
white = (255, 255, 255)
blue = (50, 153, 213)
red = (255, 0, 0)
green = (0, 255, 0)

# Game variables
snake_block = 20        # Size of each block of the snake
snake_speed = 15        # Speed of the snake

# Set up display
dis = pygame.display.set_mode((screen_width, screen_height))    
pygame.display.set_caption('Snake Game')

# Load images
snake_img = pygame.image.load('snake.png')
food_img = pygame.image.load('eat.png')
background_img = pygame.image.load('background.png')

# Load sounds
pygame.mixer.music.load('background.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')
eat_sound = pygame.mixer.Sound('eat.wav')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
    game_over = False
    game_close = False
    
    # Initial position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Change in position (movement)
    x1_change = 0
    y1_change = 0

    # List to store the snake's body
    snake_list = []
    length_of_snake = 1    

    # Position of the food
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0    
    
    pygame.mixer.music.play(-1)  # Play background music indefinitely

    # Main game loop
    while not game_over:
        while game_close == True:
            message("You Lost! Press Q-Quit or C-Play Again", blue)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for collision with walls
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            pygame.mixer.music.stop()
            game_over_sound.play()
            # game_over = True
            game_close = True
            
        
        # Check for collision with the Snake's Own Body
        for block in snake_list[:-1]:
            if block == snake_head:
                pygame.mixer.music.stop()
                game_over_sound.play()                
                # game_over = True
                game_close = True
        
        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
                        
        # Draw a rectangle
        # pygame.draw.rect(dis, blue, [150, 150, 50, 50])
        # pygame.draw.circle(dis, red, [400, 300], 50)
        # pygame.draw.line(dis, green, [0, 0], [screen_width, screen_height], 5)

        # Fill the screen with a color
        # dis.fill(white)
        dis.blit(background_img, (0, 0))

        # Draw the food
        # pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        dis.blit(food_img, (foodx, foody))
                
        # Update the snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
                
        for x in snake_list:
            # pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])
            dis.blit(snake_img, (x[0], x[1]))

        your_score(length_of_snake - 1)

        # Update the display
        pygame.display.update()
        
        # Check for collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1       
            eat_sound.play() 

        # Set the speed of the snake
        clock.tick(snake_speed)
        
        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

# Call the main loop
game_loop()
