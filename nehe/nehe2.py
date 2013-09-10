from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

from OpenGL.GL import *

class TestContext(BaseContext):
    initialPosition = (0, 0, 0)
    def Render(self, mode):
        glDisable(GL_CULL_FACE)
        glTranslate(-1.5, 0.0, -6.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()


        glTranslate(3.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()

if __name__ == "__main__":
    TestContext.ContextMainLoop()
