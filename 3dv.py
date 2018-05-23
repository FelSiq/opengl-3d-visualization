from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
SCALE_FACTOR_MIN=0.0
ENABLE_RENDER=True

def setup():
    """
    """

def drawSubtitles(text):
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
    elif key == b'':
        

    if ENABLE_RENDER:
        ENABLE_RENDER=False
        render(0)

def drawCube(edgeSize):
    """
    """
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z)
    glEnd()

def drawPentagonalPrims(edgeSize):
    """
    """

def drawHexagonalPyramid(radius, height):
    """
    """

def drawObject(id, args):
    """
    Make all transformations here...
    """
    glLoadIndentity()
    glRotatef(X_OBJECT_ANGLE, 1, 0, 0)
    glRotatef(Y_OBJECT_ANGLE, 0, 1, 0)
    glRotatef(Z_OBJECT_ANGLE, 0, 0, 1)
    glScale3f()
    glTranslate3f()

    """
    Call the function that draws the object via id
    """
    if id == 0: # Cube
        drawCube(args[0])
    elif id == 1: # Petagonal Prims
        drawPentagonalPrims(args[0])
    elif id == 2: # Hexagonal Pyramid
        drawHexagonalPyramid(args[0], ...)

def render(value):
    """
    Função limpa os buffers e chama a função drawObject
    """
    # 1. Clean buffers

    # 2. Load identity matrix

    # 3. Load projection matrix
    glOrtho(2, -2, 2, -2, 2, -100)

    # 4. Draw object (passing the id)

    # 4.b Draw text

    # 5. Call glutSwapBuffers (because 2 buffers)
    # 1 --> glFlush
    # 2 --> glutSwapBuffers()

    # ...
    global ENABLE_RENDER
    ENABLE_RENDER=True

if __name__ == '__main__':
    
