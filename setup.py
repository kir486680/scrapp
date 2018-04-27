from cx_Freeze import setup, Executable

base = None


executables = [Executable("first.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Hi",
    options = options,
    version = "0.0.1",
    description = 'Hi',
    executables = executables
)
