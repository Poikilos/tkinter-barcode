from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
		 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]

setup(
    name='Whatever',
    description='A brief description of your program.',
    version='1.3.3.7',
    options={'build_exe': {'include_files': include_files}},
    executables=[Executable('gui_barcode_printer.py', 
			    targetName='gui.exe',  
			    base='Win32GUI')]
)
