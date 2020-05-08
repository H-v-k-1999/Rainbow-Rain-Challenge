# Importing the pygame library to visualize the rain.
# If you do not have pygame installed bring up your cmd and run
# pip install pygame
# and you are ready to go.

import pygame
import random # To randomly allocate a new location to a raindrop.

pygame.init() # Initializing the pygame module.

# I wanted it to run on the full screen but unfortunately this is the
# max resolution pygame can render. If I am not correct please pull a request.

WIDTH, HEIGHT = 1280, 752

# Setting the mode to fullscreen
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# For the sake of title of the window, but in fullscreen mode it is unnecessary.
pygame.display.set_caption("Rainbow Rain Challenge")

# To control the frame rate of the screen.
clock = pygame.time.Clock()

# Declaring the backgroud color and
# the color of the raindrops
BG_COLOUR = (0, 0, 0)
BG_COLOUR_ALTERED = (153, 255, 255)

# Yeah, I accept these are not the exact rainbow colors but I liked them.
# Feel free to choose your own colors or add some more of your choice.
COLORS = [
	(132,177,250),
	(255,77,77),
	(255,151,77),
	(255,234,77),
	(145,255,77)
	(77, 255, 187),
	(77, 228, 255),
	(77, 101, 255),
	(172, 77, 255),
	(255, 77, 208)
]

# The background music
music = pygame.mixer.music.load('Not_Much_To_Say + Rain.mp3')
pygame.mixer.music.play(-1) # This will keep the music repeating


# The RainDrop class
class RainDrop(object):
	def __init__(self):
		self.x = random.randint(0, WIDTH) # Randomly choosing x coordinate on the screen
		self.y = random.randint(-100, 0) #  Randomly choosing y coordinate on the screen
		self.width = random.randint(2, 4) # Randomly choosing width of the raindrop
		self.height = random.randint(5, 7) # Randomly choosing height of the raindrop
		self.vel = random.randint(2,10) # Randomly choosing velocity of the raindrop
		self.color = COLORS[random.randint(0,len(COLORS)-1)] # Randomly assigning one of the color to the raindrop

	def move(self):
		self.y += self.vel # Increasing the y coordinate of the raindrop by the velocity of the raindrop
		if self.y == HEIGHT: # If it reaches the bottom of the screen
			self.y = -10
			self.x = random.randint(0, WIDTH)

	def draw(self, win):
		# MOMENT OF TRUTH! Our raindrop is a rectangle
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

# Initializing the raindrop array/list.
rainDrops = [RainDrop()]

run = True # To toggle the main while loop
bg_alter = False # To toggle the background of the screen

while run:

	clock.tick(100) # Keeping 100 frames a second.

	# To keep check of all events
	for event in pygame.event.get():
		# QUIT Event
		if event.type == pygame.QUIT:
			run = False
		# Key press event
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: # To check if the spacebar is pressed.
				bg_alter = not bg_alter
			if event.key == pygame.K_q or event.key == pygame.K_ESCAPE: # To check if q or esc key is pressed.
				run = False

	# To populate the raindrops array / list
	if len(rainDrops) < 2000:
		rainDrops.append(RainDrop())

	# Moving each and every raindrop and renering it on the screen.
	for drop in rainDrops:
		drop.move()
		drop.draw(win)

	# Updating the display
	pygame.display.update()

	# Altering the background color
	if bg_alter:
		win.fill(BG_COLOUR_ALTERED)
	else:
		win.fill(BG_COLOUR)

# Safely exiting the pygame
pygame.quit()