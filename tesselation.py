import sys, pygame, math, numpy
from pygame import gfxdraw
print "The best tesselation ever"

pygame.init()

size = width, height = 640,640
center = width/2, height/2
black = 0, 0, 0
gray = 40,40,40
white = 100,100,100

screen = pygame.display.set_mode(size)

t = 0
tdir = 1
tstep = 0.2
tmax = 7

points = 20
pointsAxis = 40

clock = pygame.time.Clock()

def drawGrid(screen,stride=10):
	
	for i in range(-pointsAxis,pointsAxis+1,1):
		startP = i*stride+center[0], -1
		endP = i*stride+center[0], height+1
		if i == 0:
			pygame.draw.line(screen, white, startP,endP)
		else:			
			pygame.draw.line(screen, gray, startP,endP)

	for i in range(-pointsAxis,pointsAxis+1,1):
		startP = -1,i*stride+center[1]
		endP = width+1,i*stride+center[1]
		if i == 0:
			pygame.draw.line(screen, white, startP,endP)
		else:			
			pygame.draw.line(screen, gray, startP,endP)

	return

def tFunction(point,M,t,stride=10):

	oldPoint = numpy.array([point[0]*stride,point[1]*stride])
	newPoint = numpy.dot(M,oldPoint)

	finalPoint = numpy.add(numpy.dot(t,oldPoint),(numpy.dot(1-t,newPoint)))

	return finalPoint.astype(int)

def generatePoints():
	A = []

	for i in range(-points,points+1,1):
		for j in range(-points,points+1,1):
			A.append([i,j])

	return A

def expFunction(t):
	return 1/(1+math.exp(-t))

a,b,c,d = 2,4,1,2

myPoint = 10,10


M = numpy.array([[a,b],[c,d]])

origins = generatePoints()

while 1:
	clock.tick(60)
	if tdir == 1:
		t += tstep
		if t > tmax:
			tdir = -1
			t = tmax
	else:
		t -= tstep
		if t < -tmax:
			tdir = 1
			t = -tmax

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	drawGrid(screen)

	for k in range(len(origins)):
		xor, yor = origins[k]
		(x, y) = tFunction(origins[k],M,expFunction(t))
				
		red = (255*(expFunction(t)*0.7+0.3),255*(yor+points)/float(2*points+1),255*(xor+points)/float(2*points+1))
		pygame.draw.circle(screen, red, (x+center[0],-y+center[1]),3,0)


	pygame.display.flip()




