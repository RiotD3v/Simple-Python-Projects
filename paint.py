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
colour = black
background = white

def draw(surf,colour,x,y):
	pygame.draw.circle(surf,colour,(x,y),10)
	pygame.display.flip() # update screen

# initialize screen
screen = pygame.display.set_mode((700,800))
pygame.display.set_caption("Paint")

# surfaces
drawing = pygame.surface.Surface((700,700))
settings = pygame.surface.Surface((700,100))
drawing.fill(background)
settings.fill(gray)

pygame.draw.rect(settings,red,[25,25,50,50],0) # will display current colour, red as placeholder

pygame.draw.rect(settings,red,[100,20,20,20],0)
pygame.draw.rect(settings,lime,[100,60,20,20],0)
pygame.draw.rect(settings,blue,[140,20,20,20],0)
pygame.draw.rect(settings,aqua,[140,60,20,20],0)
pygame.draw.rect(settings,fuchsia,[180,20,20,20],0)
pygame.draw.rect(settings,yellow,[180,60,20,20],0)
pygame.draw.rect(settings,navy,[220,20,20,20],0)
pygame.draw.rect(settings,teal,[220,60,20,20],0)
pygame.draw.rect(settings,green,[260,20,20,20],0)
pygame.draw.rect(settings,purple,[260,60,20,20],0)
pygame.draw.rect(settings,maroon,[300,20,20,20],0)
pygame.draw.rect(settings,olive,[300,60,20,20],0)
pygame.draw.rect(settings,silver,[340,20,20,20],0)
pygame.draw.rect(settings,black,[340,60,20,20],0)
pygame.draw.rect(settings,white,[380,20,20,20],0)

while True:
	# add surfaces + update
	screen.blit(drawing,(0,0))
	screen.blit(settings,(0,700))
	pygame.display.flip()

	for event in pygame.event.get():
		# mouse down
		if event.type == pygame.MOUSEBUTTONDOWN:
			press = True

		# mouse up
		if event.type == pygame.MOUSEBUTTONUP:
			press = False

		# draw if mouse down
		if press == True:
			(x,y) = pygame.mouse.get_pos()
			draw(drawing,colour,x,y)

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
