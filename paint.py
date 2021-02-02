import pygame

# vars
red = (255,0,0)
lime = (0,255,0)
blue = (0,0,255)
aqua = (0,255,255)
fuchsia = (255,0,255)
yellow = (255,255,0)
navy = (0,0,128)
teal = (0,128,128)
green = (0,128,0)
purple = (128,0,128)
maroon = (128,0,0)
olive = (128,128,0)
silver = (192,192,192)
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

press = False
currentcolour = black
currentsize = 10
background = white

# initialize screen
screen = pygame.display.set_mode((700,800))
pygame.display.set_caption("Paint")

# surfaces
drawing = pygame.surface.Surface((700,700))
settings = pygame.surface.Surface((700,100))
drawing.fill(background)
settings.fill(gray)

pygame.draw.rect(settings,currentcolour,[25,25,50,50],0) # will display current colour

# drawing setting boxes
redbox = pygame.draw.rect(settings,red,[100,20,20,20],0)
limebox = pygame.draw.rect(settings,lime,[100,60,20,20],0)
bluebox = pygame.draw.rect(settings,blue,[140,20,20,20],0)
aquabox = pygame.draw.rect(settings,aqua,[140,60,20,20],0)
fuchsiabox = pygame.draw.rect(settings,fuchsia,[180,20,20,20],0)
yellowbox = pygame.draw.rect(settings,yellow,[180,60,20,20],0)
navybox = pygame.draw.rect(settings,navy,[220,20,20,20],0)
tealbox = pygame.draw.rect(settings,teal,[220,60,20,20],0)
greenbox = pygame.draw.rect(settings,green,[260,20,20,20],0)
purplebox = pygame.draw.rect(settings,purple,[260,60,20,20],0)
maroonbox = pygame.draw.rect(settings,maroon,[300,20,20,20],0)
olivebox = pygame.draw.rect(settings,olive,[300,60,20,20],0)
silverbox = pygame.draw.rect(settings,silver,[340,20,20,20],0)
blackbox = pygame.draw.rect(settings,black,[340,60,20,20],0)
whitebox = pygame.draw.rect(settings,white,[380,20,20,20],0)

boxes = [(redbox,red),(limebox,lime),(bluebox,blue),(aquabox,aqua),(fuchsiabox,fuchsia),
(yellowbox,yellow),(navybox,navy),(tealbox,teal),(greenbox,green),(purplebox,purple),
(maroonbox,maroon),(olivebox,olive),(silverbox,silver),(blackbox,black),(whitebox,white)]

def draw(surf,colour,size,x,y):
	pygame.draw.circle(surf,colour,(x,y),size)
	pygame.display.flip() # update screen

def chanegcolour(box,colour,x,y):
	global currentcolour
	if box.collidepoint(x,y):
		currentcolour = colour
		pygame.draw.rect(settings,currentcolour,[25,25,50,50],0)

while True:
	# add surfaces + update
	screen.blit(drawing,(0,0))
	screen.blit(settings,(0,700))
	pygame.display.flip()

	for event in pygame.event.get():
		# mouse down
		if event.type == pygame.MOUSEBUTTONDOWN:
			press = True
			x = pygame.mouse.get_pos()[0]
			y = (pygame.mouse.get_pos()[1])-700

			# check to see if click is to change colour
			for box in boxes:
				chanegcolour(box[0],box[1],x,y)

		# mouse up
		if event.type == pygame.MOUSEBUTTONUP:
			press = False

		# draw if mouse down
		if press == True:
			(x,y) = pygame.mouse.get_pos()
			draw(drawing,currentcolour,currentsize,x,y)

		# key press
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_e:
				colour = background

			if event.key == pygame.K_d:
				colour = black

		# exit program
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
