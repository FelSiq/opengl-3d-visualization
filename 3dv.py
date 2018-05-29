#!/usr/bin/python3

"""
	Group:

	Bruno Mendes da Costa	9779433
	Felipe Alves Siqueira	9847706
	Josué Grâce Kabongo Kalala 9770382

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
LIMIT_COORD=1.0
ROTATION_INC=2.0
TRANSLATION_INC=0.025
SCALE_FACTOR_INC=0.05
SCALE_FACTOR=1.0
SCALE_FACTOR_MAX=1.0
SCALE_FACTOR_MIN=0.025
SCALE_X_SIGNAL=1.0
SCALE_Y_SIGNAL=1.0
SCALE_Z_SIGNAL=1.0
ENABLE_RENDER=True
SHOW_AXIS=True
OBJECT_ARGUMENTS=[0, 0.10, 0.25, 20, 40]
COLOR_R=1.0
COLOR_G=1.0
COLOR_B=1.0
PROJECTION_ID=0	

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
		'\n1: drawTorus' +\
		'\n2: drawPrism' +\
		'\n3: drawPyramid' +\
		'\n4: Orthogonal Projection (default)' +\
		'\n5: Perspective Projection' +\
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
		'\nb: x_mirror' +\
		'\nn: y_mirror' +\
		'\nm: z_mirror' +\
		'\n+: +zoom' +\
		'\n-: -zoom' +\
		'\nt: toggle axis' +\
		'\nr: RESET' +\
		'\nESC: exit' +\
		'\n\nParameters:' +\
		'\nX=' + str(round(X_COORD, 2)) +\
		'\nY=' + str(round(Y_COORD, 2)) +\
		'\nZ=' + str(round(Z_COORD, 2)) +\
		'\nX_angle=' + str(round(X_OBJECT_ANGLE, 2)) +\
		'\nY_angle=' + str(round(Y_OBJECT_ANGLE, 2)) +\
		'\nZ_angle=' + str(round(Z_OBJECT_ANGLE, 2)) 
	glColor3f(0.75, 0.75, 0.1)
	glLoadIdentity()
	
	yPos = 0.90
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
	global OBJECT_ARGUMENTS
	global SCALE_X_SIGNAL
	global SCALE_Y_SIGNAL
	global SCALE_Z_SIGNAL
	global SCALE_FACTOR
	global PROJECTION_ID

	# DRAW OBJECTS
	if key == b'1':
		OBJECT_ARGUMENTS=[0, 0.10, 0.25, 20, 40]		
	elif key == b'2':
		OBJECT_ARGUMENTS=[1, 0.25, 0.75, 20, 20]		
	elif key == b'3':
		OBJECT_ARGUMENTS=[2, 0.25, 3, 0.0, 0.0]		

	# PROJECTIONS COMMANDS
	elif key == b'4':
		PROJECTION_ID=0
	elif key == b'5':
		PROJECTION_ID=1
	
	# SCALE COMMANDS
	elif key == b'+':
		SCALE_FACTOR = min(SCALE_FACTOR_MAX, 
				SCALE_FACTOR + SCALE_FACTOR_INC)
	elif key == b'-':
		SCALE_FACTOR = max(SCALE_FACTOR_MIN, 
				SCALE_FACTOR - SCALE_FACTOR_INC)

	# TRANSLATION COMMANDS
	elif key == b'd':		
		X_COORD = min(LIMIT_COORD, X_COORD + TRANSLATION_INC)		
	elif key == b'a':
		X_COORD = max(-LIMIT_COORD, X_COORD - TRANSLATION_INC)
	elif key == b'e':
		Y_COORD = min(LIMIT_COORD, Y_COORD + TRANSLATION_INC)		
	elif key == b'q':
		Y_COORD = max(-LIMIT_COORD, Y_COORD - TRANSLATION_INC)
	elif key == b's':
		Z_COORD = min(LIMIT_COORD, Z_COORD + TRANSLATION_INC)		
	elif key == b'w':
		Z_COORD = max(-LIMIT_COORD, Z_COORD - TRANSLATION_INC)
	
	# ROTATION COMMANDS
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

	# MIRRORING
	elif key == b'b':
		SCALE_X_SIGNAL = -SCALE_X_SIGNAL
	elif key == b'n':
		SCALE_Y_SIGNAL = -SCALE_Y_SIGNAL
	elif key == b'm':
		SCALE_Z_SIGNAL = -SCALE_Z_SIGNAL

	# SHOW AXIS
	elif key == b't':
		SHOW_AXIS = not SHOW_AXIS

	# RESET
	elif key == b'r':
		X_OBJECT_ANGLE=30.0
		Y_OBJECT_ANGLE=30.0
		Z_OBJECT_ANGLE=30.0
		SCALE_X_SIGNAL=1.0
		SCALE_Y_SIGNAL=1.0
		SCALE_Z_SIGNAL=1.0
		X_COORD=0.0
		Y_COORD=0.0
		Z_COORD=0.0
		SCALE_FACTOR=1.0

	# EXIT
	elif key == b'\x1b': 
		# ESC KEY
		print('Program is now exiting...')
		exit(0)

	if ENABLE_RENDER:
		ENABLE_RENDER=False
		render()

def drawWireTorus(innerRadius, outerRadius, nsides, rings):
	glutWireTorus(innerRadius, outerRadius, nsides, rings)
	
def drawPentagonalPrism(baseEdgeSize, height):
	"""
	Draws a Prims with a Pentagonal base.
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

def drawHexagonalPyramid(width, height):
	"""
	Draws a Pyramid with an hexagonal base
	"""

	# 1. Defining all the vertexes of the object
	vertexes = ((width,0,0),(width/2,0,width),(-width/2,0,width),
		(-width,0,0),(-width/2,0,-width),(width/2,0,-width),(0,height*width,0))
	
	#2. Defining all the edges (conections between vertexes) of the object
	edges = ((0,1),(0,5),(0,6),(1,2),(1,6),
		(2,3),(2,6),(3,4),(3,6),(4,5),(4,6),(5,6))

	#3. Especify that we will draw lines
	glBegin(GL_LINES)

	#4. Connecting everything
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertexes[vertex])
	
	glEnd()

def drawObject(args):
	"""
	Call the function that draws the object via id
	"""
	id = args[0]
	if id == 0: # Wire Torus
		drawWireTorus(args[1], args[2], args[3], args[4])
	elif id == 1: # Petagonal Prims
		drawPentagonalPrism(args[1], args[2])
	elif id == 2: # Hexagonal Pyramid
		drawHexagonalPyramid(args[1], args[2])
	else:
		raise ValueError('First argument of \'args\'',
			'must be a integer between 0, 1 or 2.')

def drawAxis():
	"""
	Draw axis of the object
	"""
	AXIS_LIM = 1.0

	glColor3f(1, 0, 0)
	glBegin(GL_LINES)
	glVertex3f(AXIS_LIM, 0, 0)
	glVertex3f(-AXIS_LIM, 0, 0)
	glVertex3f(AXIS_LIM-0.1, -0.025, -0.025)
	glVertex3f(AXIS_LIM, 0, 0)
	glVertex3f(AXIS_LIM-0.1, 0.025, 0.025)
	glVertex3f(AXIS_LIM, 0, 0)
	glEnd()

	glColor3f(0, 1, 0)
	glBegin(GL_LINES)
	glVertex3f(0, AXIS_LIM, 0)
	glVertex3f(0, -AXIS_LIM, 0)
	glVertex3f(-0.025, AXIS_LIM-0.1, -0.025)
	glVertex3f(0, AXIS_LIM, 0)
	glVertex3f(0.025, AXIS_LIM-0.1, 0.025)
	glVertex3f(0, AXIS_LIM, 0)
	glEnd()

	glColor3f(0, 0, 1)
	glBegin(GL_LINES)
	glVertex3f(0, 0, AXIS_LIM)
	glVertex3f(0, 0, -AXIS_LIM)
	glVertex3f(-0.025, -0.025, AXIS_LIM-0.025)
	glVertex3f(0, 0, AXIS_LIM)
	glVertex3f(0.025, 0.025, AXIS_LIM-0.025)
	glVertex3f(0, 0, AXIS_LIM)
	glEnd()

def chooseProjection(id):
	
	#Orthogonal Projection
	if id == 0 :
		glOrtho(2, -2, 2, -2, 2, -100)

	#Perspective Projection (OpenGL)
	elif id == 1 :
		glFrustum(-2, 2, -2, 2, 2, 100)

def makeTransformations():
	# Load identity matrix
	glLoadIdentity()

	# Choose projection type
	chooseProjection(PROJECTION_ID)

	"""
	Make all transformations here...
	"""
	glLoadIdentity()
	glRotatef(X_OBJECT_ANGLE, 1, 0, 0)
	glRotatef(Y_OBJECT_ANGLE, 0, 1, 0)
	glRotatef(Z_OBJECT_ANGLE, 0, 0, 1)

	# Draw axis
	if SHOW_AXIS:
		drawAxis()

	glTranslatef(X_COORD, Y_COORD, Z_COORD)

	glScalef(
		SCALE_X_SIGNAL*SCALE_FACTOR, 
		SCALE_Y_SIGNAL*SCALE_FACTOR, 
		SCALE_Z_SIGNAL*SCALE_FACTOR)


def render():
	# Clean buffers (Color and Depth buffers)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Make all transformations
	makeTransformations()

	# Set object color...
	# idk what buttons should control these... to be implemented...
	glColor3f(COLOR_R, COLOR_G, COLOR_B)

	# Draw object (passing the id)
	drawObject(OBJECT_ARGUMENTS)

	# Draw text
	drawSubtitles()

	# Call glutSwapBuffers (because 2 buffers)
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
