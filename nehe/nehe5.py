from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

from OpenGL.GL import *
import time

class TestContext(BaseContext):
    initialPosition = (0, 0, 0)
    def __init__(self):
        BaseContext.__init__(self)
        self.num = 0
    def OnIdle(self):
        self.triggerRedraw(1)
        return 1

    def Render(self, mode = 0):
        BaseContext.Render(self, mode)
        glDisable(GL_LIGHTING)
        
        glTranslate(-1.5, 0.0, -6.0)
        glRotated(time.time()%(3.0)/3 * 360, num, 1, 0)
        self.drawPyramid()

    def drawPyramid( self ):
        """Draw a multicolored pyramid"""
        glBegin(GL_TRIANGLES);
        glColor3f(1.0,0.0,0.0)
        glVertex3f( 0.0, 1.0, 0.0)
        glColor3f(0.0,1.0,0.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glColor3f(0.0,0.0,1.0)
        glVertex3f( 1.0,-1.0, 1.0)
        glColor3f(1.0,0.0,0.0)
        glVertex3f( 0.0, 1.0, 0.0)
        glColor3f(0.0,0.0,1.0)
        glVertex3f( 1.0,-1.0, 1.0);
        glColor3f(0.0,1.0,0.0); 
        glVertex3f( 1.0,-1.0, -1.0);
        glColor3f(1.0,0.0,0.0);
        glVertex3f( 0.0, 1.0, 0.0);
        glColor3f(0.0,1.0,0.0);
        glVertex3f( 1.0,-1.0, -1.0);
        glColor3f(0.0,0.0,1.0);
        glVertex3f(-1.0,-1.0, -1.0);
        glColor3f(1.0,0.0,0.0);
        glVertex3f( 0.0, 1.0, 0.0);
        glColor3f(0.0,0.0,1.0);
        glVertex3f(-1.0,-1.0,-1.0);
        glColor3f(0.0,1.0,0.0);
        glVertex3f(-1.0,-1.0, 1.0);
        glEnd()

if __name__ == "__main__":
    TestContext.ContextMainLoop()
