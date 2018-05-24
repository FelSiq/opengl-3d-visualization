"""
	Group:

	B...
	Felipe Alves Siqueira	9847706
	J...

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


"""
Configuration variables section

Draw a pentadiagonal 
function(x, y, l) { 
    points = NULL; 
    for (k in 72*(0:4)) points = rbind(points, c((x - l*0.5)*cos(0.4*pi*k), (y + tan(0.3*pi/2)*l)*sin(0.4*pi*k))); 
    return (points) 
}

"""

WINDOW_WIDTH=1080
WINDOW_HEIGHT=640
X_OBJECT_ANGLE=0
Y_OBJECT_ANGLE=0
Z_OBJECT_ANGLE=0
X_COORD=0
Y_COORD=0
Z_COORD=0
ROTATION_INC=2
TRANSLATION_INC=0.025
SCALE_FACTOR_INC=0.05
SCALE_FACTOR=1.0
SCALE_FACTOR_MAX=1.0
SCALE_FACTOR_MIN=0.025
ENABLE_RENDER=True

def setup():
	"""
	Set up everything needed on for the gl/glu/glut.
	"""
	glutInit()

	# Set options for the glut display mode
	# GLUT_DOUBLE	: Double buffered window, helps reducing image flickering 
	# GLUT_RGBA	: Set a window with RGBA color mode (this actually is the default value)
	# GLUT_DEPTH	: Set a window with depth buffer
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

	# Set the program window dimensions
	glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

	# Create a window with the specified title
	glutCreateWindow('3D visualization benchmark')

	# GL_DEPTH_TEST: Enable the depth buffer (for depth comparisons)
	glEnable(GL_DEPTH_TEST)
	
	# Make sure that the color buffers are clean (all black in this case,
	# but could easily be another color)
	glClearColor(0,0,0,0) # R G B A

def drawSubtitles():
	"""
	"""

def inputEvents(key, x, y):
	"""
	Map all input keys
	"""
	global X_OBJECT_ANGLE
	global Y_OBJECT_ANGLE
	global Z_OBJECT_ANGLE
	global X_COORD
	global Y_COORD
	global Z_COORD
	global SCALE_FACTOR
	global ENABLE_RENDER

	if key == b'+':
		SCALE_FACTOR = min(SCALE_FACTOR_MAX, 
				SCALE_FACTOR + SCALE_FACTOR_INC)
	elif key == b'-':
		
		SCALE_FACTOR = max(SCALE_FACTOR_MIN, 
				SCALE_FACTOR - SCALE_FACTOR_INC)
	elif key == b'\x1b': 
		# ESC KEY
		print('Program is now exiting...')
		exit(0)

	# Must implement all keyboard events right here with
	# more elifs......

	if ENABLE_RENDER:
		ENABLE_RENDER=False
		render(0)

def drawCube(edgeSize):
	"""
	"""

def drawPentagonalPrims(BaseEdgeSize, Height):
	"""
	Draws a Prims with a Pentagonal base.
	"""
    glBegin(GL_LINE_STRIP)

    

    glEnd()

def drawHexagonalPyramid(radius, height):
	"""
	"""

def drawObject(args):
	"""
	Make all transformations here...
	"""
	glLoadIdentity()
	glRotatef(X_OBJECT_ANGLE, 1, 0, 0)
	glRotatef(Y_OBJECT_ANGLE, 0, 1, 0)
	glRotatef(Z_OBJECT_ANGLE, 0, 0, 1)
	# glScale3f() must implement...
	# glTranslate3f() must implement...

	"""
	Call the function that draws the object via id
	"""
	id = args[0]
	if id == 0: # Cube
		drawCube(args[1])
	elif id == 1: # Petagonal Prims
		drawPentagonalPrims(args[1])
	elif id == 2: # Hexagonal Pyramid
		drawHexagonalPyramid(args[1])
	else:
		raise ValueError('First argument of \'args\'',
			'must be a integer between 0, 1 or 2.')

def render(value):
	# 1. Clean buffers (Color and Depth buffers)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# 2. Load identity matrix
	glLoadIdentity()

	# 3. Load projection matrix
	glOrtho(2, -2, 2, -2, 2, -100)

	# 4. Draw object (passing the id)
	drawObject(value)

	# 4.b Draw text
	drawSubtitles()

	# 5. Call glutSwapBuffers (because 2 buffers)
	# 1 --> glFlush --> For single buffers
	# 2 --> glutSwapBuffers() --> For (and only for) 
	#	double buffered windows: "An implicit glFlush 
	# 	is done by glutSwapBuffers before it returns."
	glutSwapBuffers()

	# ...
	global ENABLE_RENDER
	ENABLE_RENDER=True

if __name__ == '__main__':

	# Set everything up in gl/glu/glut
	setup()

	# Select the function that the glut must listen for input events
	glutKeyboardFunc(inputEvents)

	# Rendering function
	render([0, 0])

	glutMainLoop()
