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

class isinserver:
    def __init__(self):
        self.serverid = None

        self.delay = 0

    def check(self, token):
        cl = client(token)

        cl.headers['Authorization'] = token

        r = cl.sess.get(
            f'https://discord.com/api/v9/guilds/{self.serverid}',
            headers=cl.headers,
            cookies=cl.cookies
        )

        log.dbg('Is in server', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Is in server', f'{token[:30]}... >> Is in >> {self.serverid}')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Is in server', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.check(token)

        elif 'Cloudflare' in r.text:
            log.warn('Is in server', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.check(token)

        elif 'captcha_key' in r.text:
            log.hcap('Is in server', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Is in server', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Is in server', error)
    
    def main(self):
        ui().prep('Is in server')
        self.serverid = ui().ask('Server ID')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Is in server', 'Delay set to 0 (failed to convert to a float, invalid input?)', False, False)
            self.delay = 0

        thread(
            files.getthreads(),
            self.check,
            files.gettokens(),
            [],
            False,
            self.delay
        )





















