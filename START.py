# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE

# Lime V2 - Official Project
# Copyright (C) 2025 R3CI
#
# This program is licensed under the GNU General Public License v3.0 (GPL-3.0).
# Unauthorized redistribution, modification, or use of this code without explicit
# permission from the owner is strictly prohibited.
#
# Official Links:
# Telegram: t.me/limev2
# Discord: discord.gg/spamming
#
# Any unauthorized use may result in takedown requests against violating repositories
# or videos using this code without permission.

# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
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
