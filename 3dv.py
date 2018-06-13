#!/usr/bin/python3

"""
	Group:

	Bruno Mendes da Costa	9779433
	Felipe Alves Siqueira	9847706
	Josué Grâce Kabongo Kalala 9770382

"""

"""
The report of this work will be submitted with the part 2.

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from collections import OrderedDict as odict

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
OBJECT_ARGUMENTS=[ 0, 0.10, 0.25, 20, 40 ]
LIGHT_POS=[ 0.0, 0.0, +10.0, 0.0 ]
PROJECTION_ID=0	
GENERAL_MAX_VAL=1.0
GENERAL_MIN_VAL=0.0
MAX_SHININESS=100.0
MIN_SHININESS=0.0
LIGHT_ARRAYS=odict()
LIGHT_ARRAYS['MAT_AMBIENT']=[ 0.5, 0.5, 0.5, 0.5 ]
LIGHT_ARRAYS['MAT_DIFFUSE']=[ 0.5, 0.5, 0.5, 0.5 ]
LIGHT_ARRAYS['MAT_EMISSION']=[ 0.5, 0.5, 0.5, 0.5 ]
LIGHT_ARRAYS['MAT_SPECULAR']=[ 0.5, 0.5, 0.5, 0.5 ]
LIGHT_ARRAYS['MAT_SHININESS']=[ 50.0 ]
LIGHT_ARRAYS['MAT_COLOR']=[ 1.0, 1.0, 1.0 ]

CURRENT_LIGHT_MAT='MAT_AMBIENT'
CURRENT_LIGHT_OPT=0

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

"""

"""
def lightInit():
	# Begin Lighting
	initLighting()

	#
	glShadeModel(GL_SMOOTH);

	# 
	glEnable(GL_LIGHTING)

	# 
	glEnable(GL_LIGHT0)
	
	# 
	glEnable(GL_COLOR_MATERIAL)

	# 
	global LIGHT_POS 
	glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POS)

	# definindo todos os componentes da luz 0)
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
	glLightfv(GL_LIGHT0, GL_SPECULAR,light_specular);
	glLightfv(GL_LIGHT0, GL_POSITION,light_position);

"""

"""
def shadingOptions():
	None

# Inicializa a luz
def initLighting():
    # Informa que irá utilizar iluminação    
    glEnable(GL_LIGHTING)
    # Liga a luz0
    glEnable(GL_LIGHT0)
    # Informa que irá utilizar as cores do material
    glEnable(GL_COLOR_MATERIAL)

# Define a posição da luz 0
def setLight():
    light_position = [10.0, 10.0, -20.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);


# Função utilizada para definir as propriedades do material
def setMaterial(currentMaterial):
    no_mat = [ 0.0, 0.0, 0.0, 1.0 ]
    mat_ambient = [ 0.7, 0.7, 0.7, 1.0 ]
    mat_ambient_color = [ 0.8, 0.8, 0.2, 1.0 ]
    mat_diffuse = [ 0.1, 0.5, 0.8, 1.0 ]
    mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
    no_shininess = [ 0.0 ]
    low_shininess = [ 5.0 ]
    high_shininess = [ 100.0 ]
    mat_emission = [0.3, 0.2, 0.2, 0.0]
    if currentMaterial ==  0:
        # Diffuse reflection only; no ambient or specular  
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat);
        glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  1:
        # Diffuse and specular reflection; low shininess; no ambient
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
        glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  2:
        # Diffuse and specular reflection; high shininess; no ambient
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    elif currentMaterial ==  3:
        # Diffuse refl.; emission; no ambient or specular reflection
        glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
        glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat);
        glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess);
        glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission);

	# Função para definir o tipo de tonalização
	def setShading(sType):
	    if sType == 0:
        	glShadeModel(GL_SMOOTH)
    	elif sType == 1:
	        glShadeModel(GL_FLAT)

"""

"""
def setMaterial():
	glMaterialfv(GL_FRONT, GL_AMBIENT, LIGHT_ARRAYS['MAT_AMBIENT'])
	glMaterialfv(GL_FRONT, GL_DIFFUSE, LIGHT_ARRAYS['MAT_DIFFUSE'])
	glMaterialfv(GL_FRONT, GL_SPECULAR, LIGHT_ARRAYS['MAT_SPECULAR'])
	glMaterialfv(GL_FRONT, GL_SHININESS, LIGHT_ARRAYS['MAT_SHININESS'])
	glMaterialfv(GL_FRONT, GL_EMISSION, LIGHT_ARRAYS['MAT_EMISSION'])


"""

"""
def brackets(i, string):
	return '['+string+']' \
		if i == CURRENT_LIGHT_OPT \
		else ' '+string+' '

"""

"""	
def drawSubtitles():
	text = 'Subtitles' +\
		'\n1: drawTorus' +\
		'\n2: drawPrism' +\
		'\n3: drawPyramid' +\
		'\n4: Orthogonal Projection' +\
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
		'\nZ_angle=' + str(round(Z_OBJECT_ANGLE, 2)) +\
		'\nzoom=' + str(round(SCALE_FACTOR*100)) + '%'

	glColor3f(0.75, 0.75, 0.10)
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

	# Subtitle related to light-related stuff
	text='  Light config:\n'
	for mat, key in zip(LIGHT_ARRAYS.keys(), ['6', '7', '8', '9', '0', ')']):
		text+= '*' if CURRENT_LIGHT_MAT==mat else ' '
		text+=' '+key+': '+mat+'\n  '
		vals=list(map(str, [round(i, 1) for i in LIGHT_ARRAYS[mat]]))
		if mat == CURRENT_LIGHT_MAT:
			for i in range(len(vals)):
				text+=brackets(i, vals[i])
		else:
			text+=' '
			text+='  '.join(vals)
		text+='\n'

	text+='commands:\n' +\
		'g: +current\n' +\
		'h: -current\n' +\
		'.: next param\n'+\
		',: prev param'
	
	glColor3f(0.05, 0.25, 0.90)
	yPos=0.90
	yInc=30.0/WINDOW_HEIGHT
	glRasterPos2f(0.60, yPos)

	for ch in text:
		if ch != '\n':
			glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))
		else:
			yPos -= yInc
			glRasterPos2f(0.60, yPos)


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
	global ENABLE_RENDER
	global SHOW_AXIS
	global OBJECT_ARGUMENTS
	global SCALE_X_SIGNAL
	global SCALE_Y_SIGNAL
	global SCALE_Z_SIGNAL
	global SCALE_FACTOR
	global PROJECTION_ID
	global GENERAL_MAX_VAL
	global GENERAL_MIN_VAL
	global MAX_SHININESS
	global MIN_SHININESS
	global LIGHT_ARRAYS
	global CURRENT_LIGHT_MAT
	global CURRENT_LIGHT_OPT

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

	# TOGGLE AXIS
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
		SCALE_X_SIGNAL=1.0 
		SCALE_Y_SIGNAL=1.0 
		SCALE_Z_SIGNAL=1.0 

	# LIGHT ARRAY PARAMETERS
	elif key == b'6':
		CURRENT_LIGHT_MAT='MAT_AMBIENT' 
	elif key == b'7':
		CURRENT_LIGHT_MAT='MAT_DIFFUSE'
	elif key == b'8':
		CURRENT_LIGHT_MAT='MAT_EMISSION' 
	elif key == b'9':
		CURRENT_LIGHT_MAT='MAT_SPECULAR' 
	elif key == b'0':
		CURRENT_LIGHT_OPT=0
		CURRENT_LIGHT_MAT='MAT_SHININESS' 
	elif key == b')':
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT, 
			len(LIGHT_ARRAYS['MAT_COLOR'])-1)
		CURRENT_LIGHT_MAT='MAT_COLOR' 

	# DECREMENT CURRENT PARAMETER OF CURRENT 
	# LIGHT CONFIG ARRAY
	elif key == b'g':
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT, 
			len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])-1)
		curVal=LIGHT_ARRAYS[CURRENT_LIGHT_MAT]\
			[CURRENT_LIGHT_OPT]
		newVal=max(GENERAL_MIN_VAL, curVal-0.1) \
			if CURRENT_LIGHT_MAT != 'MAT_SHININESS' \
			else max(MIN_SHININESS, curVal-1.0)

		LIGHT_ARRAYS[CURRENT_LIGHT_MAT]\
			[CURRENT_LIGHT_OPT]=newVal

	# INCREMENT CURRENT PARAMETER OF CURRENT 
	# LIGHT CONFIG ARRAY
	elif key == b'h':
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT, 
			len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])-1)
		curVal=LIGHT_ARRAYS[CURRENT_LIGHT_MAT]\
			[CURRENT_LIGHT_OPT]
		newVal=min(GENERAL_MAX_VAL, curVal+0.1) \
			if CURRENT_LIGHT_MAT != 'MAT_SHININESS' \
			else min(MAX_SHININESS, curVal+1.0)

		LIGHT_ARRAYS[CURRENT_LIGHT_MAT]\
			[CURRENT_LIGHT_OPT]=newVal

	# 
	elif key == b',':
		n=len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])
		CURRENT_LIGHT_OPT=(CURRENT_LIGHT_OPT-1)%n
	elif key == b'.':
		n=len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])
		CURRENT_LIGHT_OPT=(CURRENT_LIGHT_OPT+1)%n

	# EXIT
	elif key == b'\x1b': 
		# ESC KEY
		print('Program is now exiting...')
		exit(0)

	if ENABLE_RENDER:
		ENABLE_RENDER=False
		render()

def drawWireTorus(innerRadius, outerRadius, nsides, rings):
	"""
	Draws a Wire Torus.
	"""
	glutSolidTorus(innerRadius, outerRadius, nsides, rings)
	
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
	
	# 2. Defining all the edges (conections between vertexes) of the object
	edges = ((0,1),(0,5),(0,6),(1,2),(1,6),
		(2,3),(2,6),(3,4),(3,6),(4,5),(4,6),(5,6))

	# 3. Especify that we will draw lines
	glBegin(GL_LINES)

	# 4. Connecting everything
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
	# Load identity matrix
	glLoadIdentity()
	
	# Orthogonal Projection
	if id == 0 :
		glOrtho(-1, 1, -1, 1, -10, 10)

	# Perspective Projection(OpenGL)
	elif id == 1 :
		glFrustum(-1, 1, -1, 1, 1, 100)

def makeTransformations():
	# Sets that will work with the projection matrix
	glMatrixMode(GL_PROJECTION)	

	# Choose projection type
	chooseProjection(PROJECTION_ID)

	# Sets the observer settings
	gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)

	# Light-related transformations
	glMatrixMode(GL_MODELVIEW)
	shadingOptions()
	setMaterial()

	glMatrixMode(GL_PROJECTION)	
	"""
	Make all transformations here...
	"""	
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

	# Define que irá trabalhar com a matriz de modelo/visão
    #glMatrixMode(GL_MODELVIEW)
    setLight()
    setShading(curShading)

	# Make all transformations
	makeTransformations()

	# Set object color...
	cR=LIGHT_ARRAYS['MAT_COLOR'][0]
	cG=LIGHT_ARRAYS['MAT_COLOR'][1]
	cB=LIGHT_ARRAYS['MAT_COLOR'][2]
	glColor3f(cR, cG, cB)

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
