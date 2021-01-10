import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def draw(screen,x,y):
	pygame.draw.circle(screen,green,(x,y),10)
	pygame.display.flip()

# initialize screen
screen = pygame.display.set_mode((1000,1000))

# draw on mouse click
while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			(x,y) = pygame.mouse.get_pos()
			draw(screen,x,y)
