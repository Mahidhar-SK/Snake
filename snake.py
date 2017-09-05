import pygame, sys, random, time


playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)  
black = pygame.Color(0, 0, 0) 
white = pygame.Color(255, 255, 255)  
brown = pygame.Color(165, 42, 42)  

fpsController = pygame.time.Clock()


def gameOver(score):
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(score, 0)
    score = 0

    pygame.display.flip()

    time.sleep(4)
    pygame.quit()
    sys.exit()


def showScore(score, choice):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)



def main():
    init_errors = pygame.init()
    score = 0
    if init_errors[1] > 0:
        print("{0} Errors occurred, exiting...".format(init_errors[1]))
        sys.exit(-1)
    else:
        print("(+) PyGame successfully initialized!")

    initFrameRate = 10

    snakePosition = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]

    foodPosition = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    direction = 'RIGHT'
    changeto = direction

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w'):
                    changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

        if direction == 'RIGHT':
            snakePosition[0] += 10
        if direction == 'LEFT':
            snakePosition[0] -= 10
        if direction == 'UP':
            snakePosition[1] -= 10
        if direction == 'DOWN':
            snakePosition[1] += 10

        snakeBody.insert(0, list(snakePosition))
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            score += 1
            if initFrameRate < 30:
                initFrameRate += 2
            foodSpawn = False
        else:
            snakeBody.pop()

        if foodSpawn == False:
            foodPosition = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        foodSpawn = True

        playSurface.fill(white)

        for pos in snakeBody:
            pygame.draw.rect(playSurface, black, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(playSurface, black, pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

        if snakePosition[0] > 710 or snakePosition[0] < 0:
            gameOver(score)
        if snakePosition[1] > 450 or snakePosition[1] < 0:
            gameOver(score)

        for block in snakeBody[1:]:
            if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
                gameOver(score)

        showScore(score, 1)
        pygame.display.flip()

        fpsController.tick(initFrameRate)


main()
