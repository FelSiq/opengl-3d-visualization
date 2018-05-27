#!/usr/bin/python3
"""
	TO DO LIST:
	- PASS ARGUMENTS CORRECTLY TO "drawObject" function
	- IMPLEMENT KEYBOARD INPUTS
	- DRAW OBJECT B
	- DRAW OBJECT C
	- FIX/IMPROVE COMMENTARIES
	- IMPLEMENT TRANSLATION
	- IMPLEMENT SCALE (ZOOM IN/OUT)	
	- SUBMIT
	- USE MORE PROJECTION TYPES (ORTHO, FRUSTUM, PERSPECTVE)
"""


"""
	Group:

	Bruno Mendes da Costa	9779433
	Felipe Alves Siqueira	9847706
	J...

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

"""
Configuration variables section

"""

WINDOW_WIDTH=1080
WINDOW_HEIGHT=640
X_OBJECT_ANGLE=30.0
Y_OBJECT_ANGLE=30.0
Z_OBJECT_ANGLE=30.0
X_COORD=0.0
Y_COORD=0.0
Z_COORD=0.0
ROTATION_INC=2.0
TRANSLATION_INC=0.025
SCALE_FACTOR_INC=0.05
SCALE_FACTOR=1.0
SCALE_FACTOR_MAX=1.0
SCALE_FACTOR_MIN=0.025
ENABLE_RENDER=True
SHOW_AXIS=True
OBJECT_ARGUMENTS=[1, 0.25, 0.75]
COLOR_R=1.0
COLOR_G=1.0
COLOR_B=1.0
PERSPECTIVE=0

def setup():
	"""
	Set up everything needed on for the gl/glu/glut.
	"""
	glutInit()

	# Set options for the glut display mode
	# GLUT_DOUBLE	: Double buffered window, helps reducing image flickering 
	# GLUT_RGBA		: Set a window with RGBA color mode (this actually is the default value)
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
	text = 'Subtitles' +\
		'\nF1: object_A' +\
		'\nF2: object_B' +\
		'\nF3: object_C' +\
		'\nd: +x_coord' +\
		'\ns: +y_coord' +\
		'\ne: +z_coord' +\
		'\na: -x_coord' +\
		'\nw: -y_coord' +\
		'\nq: -z_coord' +\
		'\nl: +x_angle' +\
		'\nk: +y_angle' +\
		'\no: +z_angle' +\
		'\nj: -x_angle' +\
		'\ni: -y_angle' +\
		'\nu: -z_angle' +\
		'\n+: +zoom' +\
		'\n-: -zoom' +\
		'\nt: show axis' +\
		'\nSPACE: mirror' +\
		'\nESC: exit'
	glColor3f(0.75, 0.75, 0.1)
	glLoadIdentity()
	
	yPos = -0.01
	yInc = 30.0/WINDOW_HEIGHT
	glRasterPos2f(-0.98, yPos)
	for ch in text:
		if ch != '\n':
			glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))
		else:
			yPos -= yInc
			glRasterPos2f(-0.98, yPos)

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
	global ENABLE_RENDER
	global SHOW_AXIS

	if key == b'+':
		SCALE_FACTOR = min(SCALE_FACTOR_MAX, 
				SCALE_FACTOR + SCALE_FACTOR_INC)
	elif key == b'-':
		SCALE_FACTOR = max(SCALE_FACTOR_MIN, 
				SCALE_FACTOR - SCALE_FACTOR_INC)
	elif key == b'l':
		X_OBJECT_ANGLE = (X_OBJECT_ANGLE + ROTATION_INC) % 360
	elif key == b'j':
		X_OBJECT_ANGLE = (X_OBJECT_ANGLE - ROTATION_INC) % 360
	elif key == b'k':
		Y_OBJECT_ANGLE = (Y_OBJECT_ANGLE + ROTATION_INC) % 360
	elif key == b'i':
		Y_OBJECT_ANGLE = (Y_OBJECT_ANGLE - ROTATION_INC) % 360
	elif key == b'o':
		Z_OBJECT_ANGLE = (Z_OBJECT_ANGLE + ROTATION_INC) % 360
	elif key == b'u':
		Z_OBJECT_ANGLE = (Z_OBJECT_ANGLE - ROTATION_INC) % 360
	elif key == b't':
		SHOW_AXIS = not SHOW_AXIS
	elif key == b'\x1b': 
		# ESC KEY
		print('Program is now exiting...')
		exit(0)

	# Must implement all keyboard events right here with
	# more elifs......

	if ENABLE_RENDER:
		ENABLE_RENDER=False
		render()

def drawCube(edgeSize):
	"""
	"""

def drawPentagonalPrims(baseEdgeSize, height):
	"""
	Draws a Prims with a Pentagonal base.

	Logic behind this implementation:

	Draw a pentadiagonal 
	function(x, y, l) { 
	    points = NULL; 
	    for (k in 72*(0:4)) points = rbind(points, 
		c((x - l*0.5)*cos(0.4*pi*k), (y + tan(0.3*pi/2)*l)*sin(0.4*pi*k))); 
	    return (points) 
	}


	A more direct but less readable implementation:
	glVertex3f(-baseEdgeSize*0.5*math.cos(0.4*math.pi*k), 
		math.tan(0.3*math.pi/2)*baseEdgeSize*math.sin(0.4*math.pi*k), 0)
	"""
	
	x=[]
	y=[]
	z=[]
	for zShift in (1, -1):
		glBegin(GL_LINE_STRIP)
		for k in range(0, 6):
			x.append(-baseEdgeSize*0.5*math.cos(0.4*math.pi*k))
			y.append(math.tan(0.3*math.pi/2)*baseEdgeSize*math.sin(0.4*math.pi*k))
			z.append(zShift*height/2.0)
			glVertex3f(x[-1], y[-1], z[-1])
		glEnd()
	
	for i in range(0, 6):
		glBegin(GL_LINES)
		glVertex3f(x[i], y[i], z[i])
		glVertex3f(x[i+6], y[i+6], z[i+6])
		glEnd()

def drawHexagonalPyramid(radius, height):
	"""
	"""

def drawObject(args):
	"""
	Call the function that draws the object via id
	"""
	id = args[0]
	if id == 0: # Cube
		drawCube(args[1])
	elif id == 1: # Petagonal Prims
		drawPentagonalPrims(args[1], args[2])
	elif id == 2: # Hexagonal Pyramid
		drawHexagonalPyramid(args[1])
	else:
		raise ValueError('First argument of \'args\'',
			'must be a integer between 0, 1 or 2.')

def drawAxis():
	"""
	Draw axis of the object
	"""
	AXIS_LIM = 1.0

	glBegin(GL_LINES)

	glColor3f(1, 0, 0)
	glVertex3f(AXIS_LIM, 0, 0)
	glVertex3f(-AXIS_LIM, 0, 0)
	glVertex3f(AXIS_LIM-0.1, -0.025, -0.025)
	glVertex3f(AXIS_LIM, 0, 0)
	glVertex3f(AXIS_LIM-0.1, 0.025, 0.025)
	glVertex3f(AXIS_LIM, 0, 0)

	glColor3f(0, 1, 0)
	glVertex3f(0, AXIS_LIM, 0)
	glVertex3f(0, -AXIS_LIM, 0)
	glVertex3f(-0.025, AXIS_LIM-0.1, -0.025)
	glVertex3f(0, AXIS_LIM, 0)
	glVertex3f(0.025, AXIS_LIM-0.1, 0.025)
	glVertex3f(0, AXIS_LIM, 0)

	glColor3f(0, 0, 1)
	glVertex3f(0, 0, AXIS_LIM)
	glVertex3f(0, 0, -AXIS_LIM)
	glVertex3f(-0.025, -0.025, AXIS_LIM-0.025)
	glVertex3f(0, 0, AXIS_LIM)
	glVertex3f(0.025, 0.025, AXIS_LIM-0.025)
	glVertex3f(0, 0, AXIS_LIM)

	glEnd()

def makeTransformations():
	# 1. Load identity matrix
	glLoadIdentity()

	# 2. Load projection matrix
	glOrtho(2, -2, 2, -2, 2, -100)
	"""
	Make all transformations here...
	"""
	glLoadIdentity()
	glRotatef(X_OBJECT_ANGLE, 1, 0, 0)
	glRotatef(Y_OBJECT_ANGLE, 0, 1, 0)
	glRotatef(Z_OBJECT_ANGLE, 0, 0, 1)
	# glScale3f() must implement...
	# glTranslate3f() must implement...


def render():
	# 1. Clean buffers (Color and Depth buffers)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# 2. Make all transformations
	makeTransformations()

	# 3. draw axis
	if SHOW_AXIS:
		drawAxis()

	# 3.a Set object color...
	# idk what buttons should control these... to be implemented...
	glColor3f(COLOR_R, COLOR_G, COLOR_B)

	# 4. Draw object (passing the id)
	drawObject(OBJECT_ARGUMENTS)

	# 4.b Draw text
	drawSubtitles()

	# 5. Call glutSwapBuffers (because 2 buffers)
	# 1 --> glFlush --> For single buffers
	# 2 --> glutSwapBuffers() --> For (and only for) 
	#	double buffered windows: "An implicit glFlush 
	# 	is done by glutSwapBuffers before it returns."
	glutSwapBuffers()

	# Enable another screen rendering call
	global ENABLE_RENDER
	ENABLE_RENDER=True

if __name__ == '__main__':

	# Set everything up in gl/glu/glut
	setup()

	# Select the function that the glut must listen for input events
	glutKeyboardFunc(inputEvents)

	# Rendering function
	render()

	glutMainLoop()
