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

class joiner:
    def __init__(self):
        self.invite = None
        self.serverid = None
        self.servername = None

        self.delay = 0

    def discoverinvite(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.get(
            f'https://discord.com/api/v9/invites/{self.invite}?inputValue={self.invite}&with_counts=true&with_expiration=true',
            headers=cl.headers,
            cookies=cl.cookies
        )

        log.dbg('Discover invite', r.text, r.status_code)

        if r.status_code == 200: 
            #log.info('Joiner [discover invite]', f'{token[:30]}... >> Discovered >> discord.gg/{self.invite}')
            pass

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Joiner [discover invite]', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.discoverinvite(token)

        elif 'Cloudflare' in r.text:
            log.warn('Joiner [discover invite]', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.discoverinvite(token)

        elif 'You need to verify' in r.text:
            log.critical('Joiner [discover invite]', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Joiner [discover invite]', error)

    def join(self, token, cl=None):
        if cl is None:
            cl = client(token)

        cl.headers['Authorization'] = token
        self.sessionid = uuid.uuid4().hex

        payload = {
            'session_id': self.sessionid
        }

        r = cl.sess.post(
            f'https://discord.com/api/v9/invites/{self.invite}',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Joiner', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Joiner', f'{token[:30]}... >> Joined >> {self.servername} >> (discord.gg/{self.invite}) ({self.serverid})')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Joiner', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.join(token)

        elif 'Cloudflare' in r.text:
            log.warn('Joiner', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.join(token)

        elif 'captcha_key' in r.text:
            log.hcap('Joiner', f'{token[:30]}... >> HCAPTCHA (COULD BE AVOIDED BY USING PAID)')

        elif 'You need to verify' in r.text:
            log.critical('Joiner', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Joiner', error)

    
    def main(self):
        # FULL BYPASS AND SOLVER ALSO PAID ONLY
        ui().prep('Joiner')
        self.invite = ui().ask('Invite')
        self.invite = discordhelper().extract_invite(self.invite)
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Joiner', 'Delay set to 0 (failed to convert to a float, invalid input?)', False, False)
            self.delay = 0

        invinfo = discordhelper().get_invite_info(self.invite)
        self.serverid = invinfo.get('guild', {}).get('id', None)
        self.servername = invinfo.get('guild', {}).get('name', None)

        log.info('JOINER', 'BETTER BYPASSING JOINER IS PAID ONLY!')

        thread(
            files.getthreads(),
            self.join,
            files.gettokens(),
            [],
            False,
            self.delay
        )































