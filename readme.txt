Structure :
programs contains python source code
resources contains aperture images
report contains the report and the figures used in it
Circ2SlitAnim contains an animation showing the transitionfrom a circular
aperture to a slit, as well as the frames used in said animation


About the programs in general :
The programs can be executed by typing 'python nameofprogram.py' in the console
on Unix-like systems or by using an editor, such as spyder.

If an error is raised concerning imageio, install it with the instructions
from http://imageio.readthedocs.io/en/latest/installation.html.

About aperture_func.py :
This program contains functions to load and modify images to be used as apertures
in the other programs. If launched alone, showcases what the loaded image will
appear as and how the modifications works.

About ft_diff.py :
This program contains a function that displays the diffraction pattern of a given
array, with a scale representing the real coordinates.
If launched alone, showcases the diffraction pattern of a square aperture.

About quad_diff.py :
Unstable at the moment. Use it at your own risk.

About GUI.py :
This program contains the code for a Graphical User Interface which regroups
the main functions of the other programs -plus a few others- in order to
make the operations more user-friendly.
