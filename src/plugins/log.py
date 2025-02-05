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
# Discord: discord.gg/flooding
#
# Any unauthorized use may result in takedown requests against violating repositories
# or videos using this code without permission.

# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
# THE ONLY OFFICIAL SOURCE https://github.com/r3cik/LimeV2-FREE
from src import *

class log:
    def info(module, message, inp=False, ts=True, checker=False):
        if not checker:
            module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()
            message = ab5.hgratient(f'[{message}]', co.gradient1, co.gradient2).strip()
        else:
            module = f'{co.green}[{module}]{co.white}'
            message = f'{co.green}[{message}]{co.white}'

        if ts:
            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '
        else:
            ts = ''

        if inp:
            input(f'{ts}{module} >> {message}{S.RESET_ALL}')
        else:
            print(f'{ts}{module} >> {message}{S.RESET_ALL}')


    def dbg(module, *message):
        if DBG:
            module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()

            if len(message) == 1 and isinstance(message[0], str):
                message = [message[0]]
            message = ' | '.join(map(str, message))

            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '

            print(f'{ts}{module} >> {co.yellow}[{message}]{S.RESET_ALL}')

    def warn(module, message):
        module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()
        message = ab5.hgratient(f'[{message}]', co.gyellow1, co.gyellow2).strip()

        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '

        print(f'{ts}{module} >> {message}{S.RESET_ALL}')

    def hcap(module, message):
        module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()
        message = ab5.hgratient(f'[{message}]', co.gcyan1, co.gcyan2).strip()

        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '

        print(f'{ts}{module} >> {message}{S.RESET_ALL}')

    def error(module, message, ts=True):
        module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()
        message = ab5.hgratient(f'[{message}]', co.gred1, co.gred2).strip()

        if not ts:
            ts = ''
        else:
            ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '

        print(f'{ts}{module} >> {message}{S.RESET_ALL}')
        
    def critical(module, message):
        module = ab5.hgratient(f'[{module}]', co.gradient1, co.gradient2).strip()
        message = ab5.hgratient(f'[{message}]', co.gred1, co.gred2).strip()

        ts = f'{co.black}{dt.now().strftime("%H|%M|%S")} '

        print(f'{ts}{module} >> {message}{S.RESET_ALL}')

    def premium_only():
        module = ab5.hgratient(f'[Main]', co.gradient1, co.gradient2).strip()
        message = ab5.hgratient('[This is a premium only feature]', co.gradient1, co.gradient2).strip()

        print(f'{module} >> {message}{S.RESET_ALL}')
    

    def errordatabase(text):
        db = {
            '10014': 'Unknown emoji',
            '30010': 'Max reactions on message',
            '40007': 'Banned token',
            '40002': 'Locked token',
            '50109': 'Invalid JSON',
            '200000': 'Automod flagged',
            '50007': 'Action not allowed',
            '50008': 'Unable to send',
            '50001': 'No access/Not inside',
            '50013': 'Missing permissions',
            '50024': 'Cant do that on this channel',
            '80003': 'Cant self friend',
            '50168': 'Not in a VC',
            '20028': 'Limited',
            '401: Unauthorized': 'Invalid token',
            'Cloudflare': 'Cloudflare',
            'captcha_key': 'Hcaptcha',
            'Unauthorized': 'Invalid token',
            'retry_after': 'Limited',
            'You need to verify': 'Locked token',
            'Cannot send messages to this user': 'Disabled DMS',
            'You are being blocked from accessing our API': 'API BAN',
            'Unknown Invite': 'Unknown Invite',
        }

        for key in db.keys():
            if key in text:
                return db[key]

        return text

















# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2025-02-05 12:58:24
def unused_seo_function_5820():
    return 'SEO boost'
# SEO-END
