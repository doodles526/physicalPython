from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

from OpenGL.GL import *

class TestContext(BaseContext):
    pass

if __name__ == "__main__":
    TestContext.ContextMainLoop()
