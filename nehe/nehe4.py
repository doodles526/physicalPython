from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

from OpenGL.GL import *
import time

class TestContext(BaseContext):
    initialPosition = (0, 0, 0)
    def OnIdle(self):
        self.triggerRedraw(1)
        return 1

    def Render(self, mode = 0):
        BaseContext.Render(self, mode)
        glDisable(GL_CULL_FACE)
        glDisable(GL_LIGHTING)
        
        glTranslate(-1.5, 0.0, -6.0)
        glRotated(time.time()%(3.0)/3 * 360, 0, 1, 0)
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0, 1, 0)
        glVertex3f(-1.0, -1.0, 0.0)
        glColor3f(0, 0, 1)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()

        glLoadIdentity()
        glTranslate(1.5, 0.0, -6.0)
        glRotated( time.time()%(3.0)/3 * -360, 0,1,0)
        glColor3f(.5, .5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()

if __name__ == "__main__":
    TestContext.ContextMainLoop()
