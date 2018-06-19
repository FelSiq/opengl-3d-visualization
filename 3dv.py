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
import re

"""
Configuration variables section
"""
SOLID_TORUS=True
SOLID_PYRAMID=True
SOLID_PRISM=True
WINDOW_WIDTH=1080
WINDOW_HEIGHT=640
X_OBJECT_ANGLE=Y_OBJECT_ANGLE=Z_OBJECT_ANGLE=30.0
X_COORD=Y_COORD=Z_COORD=0.0
LIMIT_COORD=1.0
ROTATION_INC=2.0
TRANSLATION_INC=0.025
SCALE_FACTOR_INC=0.05
SCALE_FACTOR=1.0
SCALE_FACTOR_MAX=1.0
SCALE_FACTOR_MIN=0.025
SCALE_X_SIGNAL=SCALE_Y_SIGNAL=SCALE_Z_SIGNAL=1.0
SHOW_AXIS=True
OBJECT_ARGUMENTS=[0, 0.10, 0.25, 20, 40]
LIGHT_AMBIENT=[0.0, 0.0, 0.0, 1.0];
LIGHT_DIFFUSE=[1.0, 1.0, 1.0, 1.0];
LIGHT_SPECULAR=[1.0, 1.0, 1.0, 1.0];
LIGHT_POSITION=[8, 5.0, 5.0, 1.0];
PROJECTION_ID=0	
GENERAL_MAX_VAL=1.0
GENERAL_MIN_VAL=0.0
MAX_SHININESS=100.0
MIN_SHININESS=0.0
LIGHT_ARRAYS=odict()
LIGHT_ARRAYS['MAT_AMBIENT']=(0.0, 0.0, 0.0)
LIGHT_ARRAYS['MAT_DIFFUSE']=[0.5, 0.0, 0.0]
LIGHT_ARRAYS['MAT_EMISSION']=[0.0, 0.0, 0.0]
LIGHT_ARRAYS['MAT_SPECULAR']=[0.7, 0.6, 0.6]
LIGHT_ARRAYS['MAT_SHININESS']=[32.0]
CURRENT_SHADING=1
CURRENT_LIGHT_MAT='MAT_AMBIENT'
CURRENT_LIGHT_OPT=0
MATERIAL_OPT=15
MATERIALS = {'emerald': ((.0215 ,.1745 ,.0215 ), (.07568 ,.61424 ,.07568 ), (.633 ,.727811 ,.633 ), .6, (1, 1, 1)),
'jade': ((.135 ,.2225 ,.1575 ), (.54 ,.89 ,.63 ), (.316228 ,.316228 ,.316228 ), .1, (1, 1, 1)),
'obsidian': ((.05375 ,.05 ,.06625 ), (.18275 ,.17 ,.22525 ), (.332741 ,.328634 ,.346435 ), .3, (1, 1, 1)),
'pearl': ((.25 ,.20725 ,.20725 ), (1 ,.829 ,.829 ), (.296648 ,.296648 ,.296648 ), .088, (1, 1, 1)),
'ruby': ((.1745 ,.01175 ,.01175 ), (.61424 ,.04136 ,.04136 ), (.727811 ,.626959 ,.626959 ), .6, (1, 1, 1)),
'turquoise': ((.1 ,.18725 ,.1745 ), (.396 ,.74151 ,.69102 ), (.297254 ,.30829 ,.306678 ), .1, (1, 1, 1)),
'brass': ((.329412 ,.223529 ,.027451 ), (.780392 ,.568627 ,.113725 ), (.992157 ,.941176 ,.807843 ), .21794872, (1, 1, 1)),
'bronze': ((.2125 ,.1275 ,.054 ), (.714 ,.4284 ,.18144 ), (.393548 ,.271906 ,.166721 ), .2, (1, 1, 1)),
'chrome': ((.25 ,.25 ,.25 ), (.4 ,.4 ,.4 ), (.774597 ,.774597 ,.774597 ), .6, (1, 1, 1)),
'copper': ((.19125 ,.0735 ,.0225 ), (.7038 ,.27048 ,.0828 ), (.256777 ,.137622 ,.086014 ), .1, (1, 1, 1)),
'gold': ((.24725 ,.1995 ,.0745 ), (.75164 ,.60648 ,.22648 ), (.628281 ,.555802 ,.366065 ), .4, (1, 1, 1)),
'silver': ((.19225 ,.19225 ,.19225 ), (.50754 ,.50754 ,.50754 ), (.508273 ,.508273 ,.508273 ), .4, (1, 1, 1)),
'black plastic': ((.0 ,.0 ,.0 ), (.01 ,.01 ,.01 ), (.50 ,.50 ,.50 ), .25, (1, 1, 1)),
'cyan plastic': ((.0 ,.1 ,.06 ), (.0 ,.50980392 ,.50980392 ), (.50196078 ,.50196078 ,.50196078 ), .25, (1, 1, 1)),
'green plastic': ((.0 ,.0 ,.0 ), (.1 ,.35 ,.1 ), (.45 ,.55 ,.45 ), .25, (1, 1, 1)),
'red plastic': ((.0 ,.0 ,.0 ), (.5 ,.0 ,.0 ), (.7 ,.6 ,.6 ), .25, (1, 1, 1)),
'white plastic': ((.0 ,.0 ,.0 ), (.55 ,.55 ,.55 ), (.70 ,.70 ,.70 ), .25, (1, 1, 1)),
'yellow plastic': ((.0 ,.0 ,.0 ), (.5 ,.5 ,.0 ), (.60 ,.60 ,.50 ), .25, (1, 1, 1)),
'black rubber': ((.02 ,.02 ,.02 ), (.01 ,.01 ,.01 ), (.4 ,.4 ,.4 ), .078125, (1, 1, 1)),
'cyan rubber': ((.0 ,.05 ,.05 ), (.4 ,.5 ,.5 ), (.04 ,.7 ,.7 ), .078125, (1, 1, 1)),
'green rubber': ((.0 ,.05 ,.0 ), (.4 ,.5 ,.4 ), (.04 ,.7 ,.04 ), .078125, (1, 1, 1)),
'red rubber': ((.05 ,.0 ,.0 ), (.5 ,.4 ,.4 ), (.7 ,.04 ,.04 ), .078125, (1, 1, 1)),
'white rubber': ((.05 ,.05 ,.05 ), (.5 ,.5 ,.5 ), (.7 ,.7 ,.7 ), .078125, (1, 1, 1)),
'yellow rubber': ((.05 ,.05 ,.0 ), (.5 ,.5 ,.4 ), (.7 ,.7 ,.04 ), .078125, (1, 1, 1))}

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

	lightInit()

# Begin Lighting
def lightInit():
	# Informa que irá utilizar iluminação    
	glEnable(GL_LIGHTING)
	
	# Liga a luz0
	glEnable(GL_LIGHT0)
	
	# Informa que irá utilizar as cores do material
	glEnable(GL_COLOR_MATERIAL)

	setLight()

	# Define the color material
	glColorMaterial(GL_FRONT, GL_SPECULAR)

# Set the light 0 positon 
def setLight():
	# Defining all light 0 components)
	glLightfv(GL_LIGHT0, GL_AMBIENT, LIGHT_AMBIENT);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, LIGHT_DIFFUSE);
	glLightfv(GL_LIGHT0, GL_SPECULAR,LIGHT_SPECULAR);
	glLightfv(GL_LIGHT0, GL_POSITION, LIGHT_POSITION);

# Define the toning type
def shadingOptions():
	if CURRENT_SHADING == 0:
		glShadeModel(GL_SMOOTH)
	elif CURRENT_SHADING == 1:
		glShadeModel(GL_FLAT)

# Set the material properties
def setMaterial():	
	global LIGHT_ARRAYS	
	# Defining the material	
	material = list (MATERIALS.keys())[MATERIAL_OPT]
	LIGHT_ARRAYS['MAT_AMBIENT'] = list (MATERIALS[material][0]) # AMBIENT
	LIGHT_ARRAYS['MAT_DIFFUSE'] = list (MATERIALS[material][1]) # DIFFUSE
	LIGHT_ARRAYS['MAT_SPECULAR'] = list (MATERIALS[material][2]) # SPECULAR
	LIGHT_ARRAYS['MAT_SHININESS'] = [MATERIALS[material][3] * 128] # SHININESS	
	
	glMaterialfv(GL_FRONT, GL_AMBIENT, list (LIGHT_ARRAYS['MAT_AMBIENT']))
	glMaterialfv(GL_FRONT, GL_DIFFUSE, list (LIGHT_ARRAYS['MAT_DIFFUSE']))
	glMaterialfv(GL_FRONT, GL_SPECULAR, list (LIGHT_ARRAYS['MAT_SPECULAR']))
	glMaterialfv(GL_FRONT, GL_SHININESS, list (LIGHT_ARRAYS['MAT_SHININESS']))

"""

"""	
def drawSubtitles():
	glDisable(GL_LIGHTING)
	text = 'Subtitles' +\
		'\n1: draw solid/wire Torus' +\
		'\n2: draw solid/wire Prism' +\
		'\n3: draw solid/wire Pyramid' +\
		'\n4: orthogonal projection' +\
		'\n5: perspective projection' +\
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
		'\nx: switch material' +\
		'\nz: flat/gouraud' +\
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

	glColor3f(1, 1, 1)	
	glLoadIdentity()
	
	mat=list(MATERIALS.keys())[MATERIAL_OPT].upper()
	glRasterPos2f(-0.02*len(mat)/2, 0.7)
	
	for ch in mat:	
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch))

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
	text='Material Config\n'
	for mat in LIGHT_ARRAYS.keys():
		text+=re.sub('MAT_', '', mat).lower()+': '
		vals=list(map(str, [round(i, 1) for i in LIGHT_ARRAYS[mat]]))
		text+=' '.join(vals)
		text+='\n'
	
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
	glEnable(GL_LIGHTING)

	# Back to light
	glColor3f(1,1,1)

"""

"""
def inputEvents(key, x, y):
	"""
	Map all input keys
	"""
	global CURRENT_LIGHT_MAT, CURRENT_LIGHT_OPT, CURRENT_SHADING, SOLID_TORUS, SOLID_PRISM, SOLID_PYRAMID, MATERIAL_OPT
	global SCALE_X_SIGNAL, SCALE_Y_SIGNAL, SCALE_Z_SIGNAL
	global X_OBJECT_ANGLE, Y_OBJECT_ANGLE, Z_OBJECT_ANGLE
	global GENERAL_MAX_VAL, GENERAL_MIN_VAL
	global MAX_SHININESS, MIN_SHININESS
	global X_COORD, Y_COORD, Z_COORD
	global OBJECT_ARGUMENTS	
	global PROJECTION_ID
	global SCALE_FACTOR
	global LIGHT_ARRAYS
	global SHOW_AXIS
	
	# DRAW OBJECTS
	if key == b'1':
		if(OBJECT_ARGUMENTS[0] == 0):
			SOLID_TORUS = not SOLID_TORUS
		OBJECT_ARGUMENTS=[0, 0.10, 0.25, 20, 40]
	elif key == b'2':
		if(OBJECT_ARGUMENTS[0] == 1):
			SOLID_PRISM = not SOLID_PRISM
		OBJECT_ARGUMENTS=[1, 0.25, 0.75, 20, 20]		
	elif key == b'3':
		if(OBJECT_ARGUMENTS[0] == 2):
			SOLID_PYRAMID = not SOLID_PYRAMID
		OBJECT_ARGUMENTS=[2, 0.25, 3, 0.0, 0.0]		

	# PROJECTIONS COMMANDS
	elif key == b'4':
		PROJECTION_ID=0
	elif key == b'5':
		PROJECTION_ID=1
	
	# SCALE COMMANDS
	elif key == b'+':
		SCALE_FACTOR = min(SCALE_FACTOR_MAX, SCALE_FACTOR + SCALE_FACTOR_INC)
	elif key == b'-':
		SCALE_FACTOR = max(SCALE_FACTOR_MIN, SCALE_FACTOR - SCALE_FACTOR_INC)

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
		X_OBJECT_ANGLE=Y_OBJECT_ANGLE=Z_OBJECT_ANGLE=30.0		
		SCALE_X_SIGNAL=SCALE_Y_SIGNAL=SCALE_Z_SIGNAL=1.0 
		X_COORD=Y_COORD=Z_COORD=0.0
		SCALE_FACTOR=1.0
		CURRENT_SHADING=1
		CURRENT_LIGHT_MAT='MAT_AMBIENT'
		CURRENT_LIGHT_OPT=0
		MATERIAL_OPT=0

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
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT,len(LIGHT_ARRAYS['MAT_COLOR'])-1)
		CURRENT_LIGHT_MAT='MAT_COLOR' 

	# DECREMENT CURRENT PARAMETER OF CURRENT 
	# LIGHT CONFIG ARRAY
	elif key == b'g':
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT,len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])-1)
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
		CURRENT_LIGHT_OPT=min(CURRENT_LIGHT_OPT,len(LIGHT_ARRAYS[CURRENT_LIGHT_MAT])-1)
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

	# LIGHT MATERIAL
	elif key == b'x' :
		MATERIAL_OPT += 1
		MATERIAL_OPT %= 24 # 4 Allows Manual Parameters		

	# SMOTH OR FLATH
	elif key == b'z' :
		CURRENT_SHADING += 1
		CURRENT_SHADING %= 2

	# EXIT
	elif key == b'\x1b': 
		# ESC KEY
		print('Program is now exiting...')
		exit(0)
	
	# REDISPLAY
	glutPostRedisplay()	
	
def drawSolidTorus(innerRadius, outerRadius, nsides, rings):
	"""
	Draws a Solid Torus.
	"""	
	glutSolidTorus(innerRadius, outerRadius, nsides, rings)

def drawWireTorus(innerRadius, outerRadius, nsides, rings):
	"""
	Draws a Wire Torus.
	"""
	glutWireTorus(innerRadius, outerRadius, nsides, rings)
	
def drawPentagonalPrism(baseEdgeSize, height, solid):
	"""
	Draws a Prims with a Pentagonal base.
	"""
	
	x=[]
	y=[]
	z=[]
	for zShift in (1, -1):
		if solid:
				glBegin(GL_POLYGON)
		else:
				glBegin(GL_LINE_STRIP)

		for k in range(0, 6):
			x.append(-baseEdgeSize*0.5*math.cos(0.4*math.pi*k))
			y.append(math.tan(0.3*math.pi/2)*baseEdgeSize*math.sin(0.4*math.pi*k))
			z.append(zShift*height/2.0)
			glVertex3f(x[-1], y[-1], z[-1])
		glEnd()
	x.append(x[0])
	y.append(y[0])
	z.append(z[0])
	

	for i in range(0, 6):
		if not solid:
			glBegin(GL_LINES)
			glVertex3f(x[i], y[i], z[i])
			glVertex3f(x[i+6], y[i+6], z[i+6])
			glEnd()
		else:
			glBegin(GL_POLYGON)
			glVertex3f(x[i], y[i], z[i])
			glVertex3f(x[i+6], y[i+6], z[i+6])
			glVertex3f(x[i+7], y[i+7], z[i+7])
			glVertex3f(x[i+1], y[i+1], z[i+1])
			glEnd()

def drawHexagonalPyramid(width, height):
	"""
	Draws a Pyramid with an hexagonal base
	"""

	# 1. Defining all the vertexes of the object
	vertexes = ((width,0,0),(width/2,0,width),(-width/2,0,width),
		(-width,0,0),(-width/2,0,-width),(width/2,0,-width),(0,height*width,0))
	
	# 2. Defining all the edges (conections between vertexes) of the object
	edges = ((0,1),(0,5),(0,6),(1,2),(1,6),(2,3),(2,6),(3,4),(3,6),(4,5),(4,6),(5,6))

	# 3. Especify that we will draw lines
	glBegin(GL_LINES)

	# 4. Connecting everything
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertexes[vertex])
	
	glEnd()

def drawSolidHexagonalPyramid(width, height):

	"""
	Draws a Pyramid with an hexagonal base
	"""

	# 1. Defining all the vertexes of the pyramid
	vertexes = ((width,0,0),(width/2,0,width),(-width/2,0,width),
		(-width,0,0),(-width/2,0,-width),(width/2,0,-width),(0,height*width,0))

	# 2. Defining surfaces of the pyramid
	surfaces = ((0,1,6),(1,2,6),(2,3,6),(3,4,6),(4,5,6),(5,0,6))

	# 3. Especify that we will draw triangles
	glBegin(GL_TRIANGLES)

	# 4. Draw the pyramid
	for surface in surfaces:
		for vertex in surface:
			glVertex3fv(vertexes[vertex])

	glEnd()

def drawObject(args):
	setMaterial()

	"""
	Call the function that draws the object via id
	"""
	id = args[0]
	if id == 0 and SOLID_TORUS == False: # Wire Torus
		drawWireTorus(args[1], args[2], args[3], args[4])
	elif id == 0 and SOLID_TORUS == True: # Solid Torus
		drawSolidTorus(args[1], args[2], args[3], args[4])
	elif id == 1 and SOLID_PRISM == False: # Wire Petagonal Prims
		drawPentagonalPrism(args[1], args[2], False)
	elif id == 1 and SOLID_PRISM == True: # Solid Petagonal Prims
		drawPentagonalPrism(args[1], args[2], True)
	elif id == 2 and not(SOLID_PYRAMID): # Wire Hexagonal Pyramid
		drawHexagonalPyramid(args[1], args[2])
	elif id == 2 and SOLID_PYRAMID: #Solid Hexagonal Pyramid
		drawSolidHexagonalPyramid(args[1], args[2])
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

	# Back to light
	glColor3f(1,1,1)

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

	# Make all transformations
	makeTransformations()  

	# Set object color...
	#cR=LIGHT_ARRAYS['MAT_COLOR'][0]
	#cG=LIGHT_ARRAYS['MAT_COLOR'][1]
	#cB=LIGHT_ARRAYS['MAT_COLOR'][2]
	#glColor3f(cR, cG, cB)

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

if __name__ == '__main__':
	# Set everything up in gl/glu/glut
	setup()

	# Rendering function
	glutDisplayFunc(render)

	# Select the function that the glut must listen for input events
	glutKeyboardFunc(inputEvents)

	glutMainLoop()
