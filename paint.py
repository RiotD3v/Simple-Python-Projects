import pygame

# vars
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
press = False

def draw(screen,colour,x,y):
	pygame.draw.circle(screen,colour,(x,y),10)
	pygame.display.flip() # update screen

# initialize screen
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Paint")

colour = white

while True:
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
			draw(screen,colour,x,y)

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
