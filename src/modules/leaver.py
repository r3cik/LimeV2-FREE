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
from src.plugins.log import *
from src.plugins.ui import *
from src.dchelper import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class leaver:
    def __init__(self):
        self.serverid = None

        self.delay = 0

    def leave(self, token):
        cl = client(token)

        payload = {
            'lurking': False,
        }

        cl.headers['Authorization'] = token

        r = cl.sess.delete(
            f'https://discord.com/api/v9/users/@me/guilds/{self.serverid}',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Leaver', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Leaver', f'{token[:30]}... >> Left >> {self.serverid}')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('Leaver', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.leave(token)

        elif 'Cloudflare' in r.text:
            log.warn('Leaver', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.leave(token)

        elif 'captcha_key' in r.text:
            log.hcap('Leaver', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Leaver', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Leaver', error)

    
    def main(self):
        ui().prep('Leaver')
        self.serverid = ui().ask('Server ID')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Leaver', 'Delay set to 0 (failed to convert to a floatl, invalid input?)', False, False)
            self.delay = 0

        thread(
            files.getthreads(),
            self.leave,
            files.gettokens(),
            [],
            False,
            self.delay
        )





















