import os
program = "venv/bin/python"
arguments = "main.py"
try:
    print("restarting...")
    os.execvp(program, (program, arguments))
except OSError as e:
    print(e)
