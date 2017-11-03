""" OpenPTV-Python is the GUI for the OpenPTV (http://www.openptv.net) liboptv library 
based on Python/Enthought Traits GUI/Numpy/Chaco

.. moduleauthors:: OpenPTV group

"""

import os, sys, inspect
sys.path.append(os.path.abspath('../src_c'))

 # realpath() will make your script run, even if you symlink it :)
 cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
 if cmd_folder not in sys.path:
     sys.path.insert(0, cmd_folder)

 # Use this if you want to include modules from a subfolder
 cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
 if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)

 # Info:
 # cmd_folder = os.path.dirname(os.path.abspath(__file__)) # DO NOT USE __file__ !!!
 # __file__ fails if the script is called in different ways on Windows.
 # __file__ fails if someone does os.chdir() before.
 # sys.argv[0] also fails, because it doesn't not always contains the path.
