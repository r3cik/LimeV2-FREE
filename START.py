import os
import subprocess
import sys

venv = 'LimeV2VENV'

if not os.path.exists(venv):
    print('Creating virtual environment...')
    subprocess.run([sys.executable, '-m', 'venv', venv])

print('Activating virtual environment...')
activate_script = os.path.join(venv, 'Scripts', 'activate.bat')
subprocess.run(activate_script, shell=True)

print('Installing dependencies from requirements.txt...')
subprocess.run([os.path.join(venv, 'Scripts', 'pip'), 'install', '-r', 'requirements.txt'])

print('Running main.py...')
subprocess.run([os.path.join(venv, 'Scripts', 'python'), 'main.py', 'LimeV2'])
input('Enter to exit')
exit()