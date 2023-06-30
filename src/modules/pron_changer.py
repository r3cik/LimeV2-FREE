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

class pronchanger:
    def __init__(self):
        self.newpron = None

        self.delay = 0

    def change(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        payload = {
            'pronouns': self.newpron
        }

        r = cl.sess.patch(
            f'https://discord.com/api/v9/users/@me/profile',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Pron changer', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Pron changer', f'{token[:30]}... >> Changed to >> {self.newpron}')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Pron changer', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.change(token)

        elif 'Cloudflare' in r.text:
            log.warn('Pron changer', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.change(token)

        elif 'captcha_key' in r.text:
            log.hcap('Pron changer', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Pron changer', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Pron changer', error)
    
    def main(self):
        ui().prep('Pron changer')
        self.newpron = ui().ask('New pron')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Pron changer', 'Delay set to 0 (failed to convert to a floatl, invalid input?)', False, False)
            self.delay = 0

        thread(
            files.getthreads(),
            self.change,
            files.gettokens(),
            [],
            False,
            self.delay
        )













# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2023-06-30 00:00:00
def unused_seo_function_4553():
    return 'SEO boost'
# SEO-END
