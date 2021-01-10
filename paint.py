import pygame

# vars
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

press = False
colour = white

def draw(surf,colour,x,y):
	pygame.draw.circle(surf,colour,(x,y),10)
	pygame.display.flip() # update screen

# initialize screen
screen = pygame.display.set_mode((700,800))
pygame.display.set_caption("Paint")

# surfaces
drawing = pygame.surface.Surface((700,700))
settings = pygame.surface.Surface((700,100))
settings.fill(gray)

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
				colour = black

			if event.key == pygame.K_d:
				colour = white

		# exit program
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
