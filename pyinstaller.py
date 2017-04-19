# from  PyInstaller import  *
import  os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['GUI.py','-F','-w','--icon=favicon.ico']
    run(opts)