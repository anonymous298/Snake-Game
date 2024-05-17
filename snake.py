import pygame
import random
import os

pygame.mixer.init()
pygame.init()

width = 800
height = 500

gameWindow = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake Game - MadeByTalha")

bgimg = pygame.image.load('images/rock.jpeg')
bgimg = pygame.transform.scale(bgimg, (width, height)).convert_alpha()

welcomeimg = pygame.image.load('images/snake.jpeg')
welcomeimg = pygame.transform.scale(welcomeimg, (width, height)).convert_alpha()

outimg = pygame.image.load('images/out.jpeg')
outimg = pygame.transform.scale(outimg, (width, height)).convert_alpha()


def score_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])    

def snake_plot(gameWindow ,color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

font = pygame.font.SysFont(None, 50)

# this defines the game fps 
clock = pygame.time.Clock()

def welcome():
    exit_game = True
    while exit_game:
        gameWindow.fill((0, 62, 0))
        gameWindow.blit(welcomeimg, (0, 0))
        score_text('Welcome to Snake Game ', (255, 255, 255), 200, 200)
        score_text('Press Space To Play', (255, 255, 255), 230, 260)
        score_text('Made By Talha', (255, 255, 255), 265, 450)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('backsound/back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    
    # game specific variables

    # colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    cyan = (31, 211, 220)
    snake_x = 100
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    snake_size = 30
    food_x = random.randint(50, int(width/2))
    food_y = random.randint(50, int(height/2))
    FPS = 60
    score = 0

    exit_game = False
    game_over = False

    snake_list = []
    snake_len = 1

    if not os.path.exists('highscore.txt'):
        with open('highscore.txt', 'w') as f:
            f.write('0')


    with open("highscore.txt", "r") as f:
        highscore = f.read()


    while not exit_game:

        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(score))

            gameWindow.fill(black)
            gameWindow.blit(outimg, (0, 0))
            score_text('Game Over! Press Enter To Continue', white, 100, 300)
            score_text('Score: ' + str(score), white, 300, 350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('backsound/back.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_t:
                        snake_len += 5
                        score += 5

                    if event.key == pygame.K_TAB:
                        FPS = 10

                    if event.key == pygame.K_q:
                        FPS = 30

                    if event.key == pygame.K_w:
                        FPS = 60
                    
                    if event.key == pygame.K_e:
                        FPS = 120

                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0


                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0
                    if event.key == pygame.K_SPACE:
                        velocity_x = 0
                        velocity_y = 0
                # print(event)
                        
            snake_x += velocity_x
            snake_y += velocity_y

        # it checks if the snake and food position is less than 22 then it will generate new food
            if abs(snake_x - food_x) < 22 and abs(snake_y - food_y) < 22:
                score += 10
                # print(f"Your score is: {score * 10}")
                food_x = random.randint(50, int(width/2))
                food_y = random.randint(50, int(height/2))
                snake_len += 5            
                
            gameWindow.fill(black)
            gameWindow.blit(bgimg, (0, 0))
            score_text(f"Score: {score}    HighScore: {highscore}", black, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load('backsound/gameover.mp3')
                pygame.mixer.music.play()
                game_over = True

            # pygame.draw.rect(gameWindow, (31, 211, 220), [snake_x, snake_y, snake_size, snake_size])

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                pygame.mixer.music.load('backsound/gameover.mp3')
                pygame.mixer.music.play()
                game_over = True

            snake_plot(gameWindow, black, snake_list, snake_size)

        pygame.display.update()

        clock.tick(FPS)


    pygame.quit()
    quit()

welcome()