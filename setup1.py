"""
Command line to run - python setup1.py build
"""
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"includes":["Tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Prakhar Gandhi",
        version = "1.0.2",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("guiFifth_barcode_printer_and_youtube_with_threading.py", base=base)])
