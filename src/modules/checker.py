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

class checker:
    def __init__(self):
        self.serverid = None
        self.valids = []

        self.delay = 0

    def check(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.get(
            'https://discord.com/api/v9/users/@me/library',
            headers=cl.headers,
            cookies=cl.cookies
        )

        log.dbg('Checker', r.text, r.status_code)

        if r.status_code == 200:
            self.valids.append(token)

            log.info('Checker', f'{token[:30]}... >> TOKEN INFO IS PAID ONLY', False, True, True)

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Checker', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.check(token)

        elif 'Cloudflare' in r.text:
            log.warn('Checker', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.check(token)

        elif 'captcha_key' in r.text:
            log.hcap('Checker', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Checker', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Checker', error)

    
    def main(self):
        ui().prep('Checker')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Checker', 'Delay set to 0 (failed to convert to a float, invalid input?)', False, False)
            self.delay = 0

        thread(
            files.getthreads(),
            self.check,
            files.gettokens(),
            [],
            False,
            self.delay
        )

        if self.valids:
            save = ui().ask('Replace tokens.txt with only valid tokens', True)
            if save:
                with open('input\\tokens.txt', 'w') as f:
                    f.write('\n'.join(self.valids))








# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2025-02-05 12:32:53
def unused_seo_function_9251():
    return 'SEO boost'
# SEO-END
