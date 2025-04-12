pip install PyOpenGL PyOpenGL_accelerate

_____________

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

_____________

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Definir a cor de fundo
    glEnable(GL_DEPTH_TEST)  # Habilitar teste de profundidade (Z-buffer)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpar o buffer de cores e profundidade
    glLoadIdentity()  # Resetar a matriz de transformação
    gluLookAt(0.0, 0.0, 5.0,  # Posição da câmera
              0.0, 0.0, 0.0,  # Ponto que a câmera está olhando
              0.0, 1.0, 0.0)  # Vetor up

    # Rotacionar o cubo
    glRotatef(1, 3, 1, 1)

    # Desenhar o cubo
    glBegin(GL_QUADS)

    # Frente
    glColor3f(1.0, 0.0, 0.0)  # Vermelho
    glVertex3f( 1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0,-1.0, -1.0)
    glVertex3f( 1.0,-1.0, -1.0)

    # Traseira
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)

    # Esquerda
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.0, 1.0,  1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0,-1.0, -1.0)
    glVertex3f(-1.0,-1.0,  1.0)

    # Direita
    glColor3f(1.0, 1.0, 0.0)  # Amarelo
    glVertex3f( 1.0, 1.0, -1.0)
    glVertex3f( 1.0, 1.0,  1.0)
    glVertex3f( 1.0,-1.0,  1.0)
    glVertex3f( 1.0,-1.0, -1.0)

    # Topo
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)

    # Base
    glColor3f(0.0, 1.0, 1.0)  # Ciano
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)

    glEnd()

    glutSwapBuffers()  # Trocar os buffers (double buffering)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def timer(fps):
    glutPostRedisplay()
    glutTimerFunc(int(1000/fps), timer, fps)

_____________

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cubo 3D Rotacionando")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 60)  # 60 FPS
    glutMainLoop()

if __name__ == "__main__":
    main()

_____________


