import os
from monitor.setup import __version__
from cx_Freeze import setup, Executable
from glob import glob


GUI2Exe_Target_1 = Executable(
    script = "main.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "MonitorCam.exe",
    #compress = True,
    #copyDependentFiles = True,
    #appendScriptToExe = False,
    #appendScriptToLibrary = False
    icon = os.path.join("resources", "images", "icon.png")
    )
excludes = ["tkinter"]
includes = ["cv2",]
#namespace_packages=["multiprocessing.pool"]
packages=["cv2"]
path = []
config_clent:str = os.path.join('monitor',"telegram","config")
include_files=[("config","config"),
               ("log","log"),
               (config_clent,config_clent),
               ("resources","resources"),
               ("token_bot.txt","token_bot.txt")]
setup(
    version = __version__,
    description = "Monitora links rstp de câmeras",
    author = "Elton Fernandes dos Santos",
    author_email = "eltonfernando90@email.com",
    name = "MonitorCam",
    options = {"build_exe": {"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "include_msvcr": True,
                            # "namespace_packages":namespace_packages,
                             "path": path,
                            'include_files':include_files
                            }
               },
    executables = [GUI2Exe_Target_1]
    )