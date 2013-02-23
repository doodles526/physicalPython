Physical Python
===============

Python package/API to aid in the education of Physics students.  The
goals are similar to those of [VPython](http://vpython.org), which is
used in the [Matter and Interactions
curriculum](http://matterandinteractions.org).  We aim for Physical
Python to both address shortcomings in vpython (particularly related
to its use in teaching programming), as well as make improvements, all
with a simpler code base composed of pure python, and an API that
lends itself to further exploration with [numpy](http://numpy.org) and
[matplotlib](http://matplotlib.org).

Shortcomings of VPython we would like to address
------------------------------------------------

1. Ordinary python assignment semantics is broken in the visual
   package.  This leads to student difficulties and hard-to-find
   bugs.

2. 2D plotting in visual the visual package gives very poor results,
   and uses an idiosyncratic API.

3. VPython has very poor support for linux.

Features we would like to add beyond those in VPython
-----------------------------------------------------

1. It would be great for students to be able to express units in their
   programs.  Even better if the interpreter is able to check for
   consistency in units.

2. It would be convenient to be able to attach objects to each other,
   so that, for instance, moving a ball would also appropriately
   adjust a spring that is attached to that ball.

3. We would like to have a matplotlib-like API for 2D plotting.
