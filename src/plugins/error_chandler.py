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
from src import *
from src.plugins.log import *

with open('output\\errors.txt', 'w') as f:
    f.write('')

def log_errors(exctype, value, tb):
    try:
        error = ''.join(traceback.format_exception(exctype, value, tb))
        log.error('Error chandler', error, False)
        try:
            with open('output\\errors.txt', 'a', encoding='utf-8') as f:
                f.write(error)
        except:
            with open('ERRORS.txt', 'a', encoding='utf-8') as f:
                f.write(error)

        # dildos = gay
        if 'KeyboardInterrupt' in exctype or 'KeyboardInterrupt' in value or 'KeyboardInterrupt' in tb:
            return
        try:
            requests.get(
                'http://us3.bot-hosting.net:20933/error-free', 
                json={
                    f'content': f'```{error}```'
                }
            )
        except:
            pass
    except:
        print(f'{exctype} - {value} - {tb}')

sys.excepthook = log_errors
