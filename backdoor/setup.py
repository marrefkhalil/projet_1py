from cx_Freeze import setup, Executable

setup(name = 'client', version = '0.1', description = 'client', executables = [Executable("client.py")])
