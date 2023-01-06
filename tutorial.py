# Import the pygame library and initialise the game engine
import pygame
import random
import math
pygame.init()

# Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)

#Variables to define sizes of the window and the paddles
screenWidth = 1280
screenHeight = 720

paddleHeight = screenHeight / 5
paddleWidth = screenWidth / 40
startingPaddleX = 10
startingPaddleY = (screenHeight / 2) - paddleHeight / 2
ballHeight = screenWidth / 50
ballWidth = screenWidth / 50

paddleVelocity = 20
ballVelocity = 2
ballAngle = random.randint(30,60) / (180 / math.pi)
ballDirection = random.choice([-1,1])
ballDirectionX = ballDirection
ballDirectionY = ballDirection
leftPaddleHeight = startingPaddleY
ballPositionX = screenWidth / 2
ballPositionY = random.randint(0,screenHeight - int(ballHeight)+1)

# Open a new window
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, colour=white):
        super(Sprite, self).__init__()
        self.paddleWidth = width
        self.paddleHeight = height
        self.colour = colour
        self.image = pygame.Surface((self.paddleWidth, self.paddleHeight))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Create the paddle and ball objects 
leftPaddle = Sprite(paddleWidth,paddleHeight)
ball = Sprite(ballWidth,ballHeight,green)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# -------- Main Program Loop -----------
while carryOn:
    screen.fill(black)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                #Move the left paddle up
                leftPaddleHeight = leftPaddleHeight - paddleVelocity
                if leftPaddleHeight < 0:
                    leftPaddleHeight = 0
            if event.key == pygame.K_z:
                #Move the left paddle down
                leftPaddleHeight = leftPaddleHeight + paddleVelocity
                if leftPaddleHeight > screenHeight - paddleHeight:
                    leftPaddleHeight = screenHeight - paddleHeight

    #Make the ball move, based on the initial random values
    ballPositionX += ballDirectionX*ballVelocity*math.cos(ballAngle)
    ballPositionY += ballDirectionY*ballVelocity*math.sin(ballAngle) 

    #When the ball reaches an extremity, we need to flip the direction
    if ballPositionY <= 0 or ballPositionY >= screenHeight - ballHeight:
        ballDirectionY *= -1

    #Now handle if the ball hits the left paddle
    if ballDirectionX == -1 and ballPositionX <= paddleWidth+startingPaddleX and ballPositionY >= leftPaddleHeight and ballPositionY <= leftPaddleHeight + paddleHeight:
        ballDirectionX *= -1
    
    #Now handle if the ball leaves the left or right side of the screen
    if ballPositionX <= 0 or ballPositionX >= screenWidth:
        ballPositionX = screenWidth / 2
        ballPositionY = random.randint(0,screenHeight - int(ballHeight)+1)
        ballAngle = random.randint(30,60) / (180 / math.pi)
        ballDirection *= -1
        ballDirectionX = ballDirection
        ballDirectionY = ballDirection

    screen.blit(leftPaddle.image,(startingPaddleX, leftPaddleHeight))
    screen.blit(ball.image, (ballPositionX,ballPositionY))
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)
     
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()