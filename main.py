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
import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *
from src.plugins.files import *
from src.plugins.error_chandler import *
from src.plugins.log import *
from src.plugins.ui import *
from src.plugins.auto_update import *

ui().cls()
ui().title(DISCORDINVITE)
ui().banner()
log.info('Main', 'Startring up!')

auto_update().auto_update()

stop = False
if not files.getproxies() and files.getproxystatus():
    log.info('Main', 'Proxies ware enabled inside of settings.json but none are inside of input\\proxies.txt the code will not work properly please input proxies or disable proxies in settings.json')
    stop = True

if not files.gettokens():
    log.info('Main', 'U did not input any tokens into input\\tokens.txt please input them in! (NOT DISCORD BOT TOKENS ACTUAL ACCOUNT TOKENS)')
    stop = True

if files.getsolverstatus():
    log.info('Main', 'Solver is paid only! Please turn it off')
    stop = True

if files.getonlinetokensstatus():
    log.info('Main', 'Token online is paid only! Please turn it off')
    stop = True

if stop:
    log.info('Main', 'Enter to continue anyway', True)

from src.modules.joiner import *
from src.modules.leaver import *
from src.modules.isinserver import *
from src.modules.message_spammer import *
from src.modules.checker import *
from src.modules.display_changer import *
from src.modules.pron_changer import *
from src.modules.reaction import *
from src.modules.combototoken import *

while True:
    ui().cls()
    ui().title(DISCORDINVITE)
    ui().banner()
    ui().stats()
    ui().menu()

    choice = ui().ask('Choice')

    options = {
        #'>>': lambda: (ui().menu2(), ui().ask('Choice')),
        '>>': log.premium_only,
        '1': joiner().main,
        '2': leaver().main,
        '3': isinserver().main,
        '4': log.premium_only,
        '5': log.premium_only,
        '6': messagespammer().main,
        '7': log.premium_only,
        '8': log.premium_only,
        '9': log.premium_only,
        '10': log.premium_only,
        '11': checker().main,
        '12': log.premium_only,
        '13': log.premium_only,
        '14': displaychanger().main,
        '15': pronchanger().main,
        '16': log.premium_only,
        '17': reaction().main,
        '18': log.premium_only,
        '19': log.premium_only,
        '20': log.premium_only,
        '21': log.premium_only,
        '22': log.premium_only,
        '23': log.premium_only,
        '24': log.premium_only,
        '25': log.premium_only,
        '26': log.premium_only,
        '27': log.premium_only,
        '28': log.premium_only,
        '29': log.premium_only,
        '30': combototoken().main,
    }

    if choice in options:
        options[choice]()
        log.info('Main', 'Finished! Enter to continue', True)
        
    else:
        log.info('Main', 'That option does not exist yet', True)
