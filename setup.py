import sys,os,requests,tkinter
from cx_Freeze import setup, Executable
os.environ['TCL_LIBRARY'] = 'C:/Users/HP/AppData/Local/Programs/Python/Python36/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/HP/AppData/Local/Programs/Python/Python36/tcl/tk8.6'
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","requests","tkinter","tkinter.ttk"],
                     "excludes":[]
                        ,"includes":["tkinter","tkinter.ttk"]
                     ,"include_files":['C:/Users/HP/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll',
           'C:/Users/HP/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll']
}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup( name = "gui",
version = "0.1",
description = "My GUI application!",
options = {"build_exe": build_exe_options},
executables = [Executable("gui_barcode_printer.py", base=base)])
