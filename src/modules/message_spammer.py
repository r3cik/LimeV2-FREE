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

class messagespammer:
    def __init__(self):
        self.serverid = None
        self.channelid = None
        self.basemsg = None
        self.tts = False
        self.ids = []

        self.delay = 0
        self.dontstop = False

    def replacer(self, match):
        tag, number = match.group(1), match.group(2)
        if tag == 'emoji':
            return discordhelper().getemojis(int(number))
        elif tag == 'str':
            return discordhelper().getstr(int(number))
        return ''

    def replace_tags(self, text):
        return re.sub(r'\[\[(str|ping|emoji)=(\d+)\]\]|\[\[.*?\]\]', self.replacer, text)

    def send(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token
        
        while True:
            discordhelper().delay(self.delay)
            message = self.replace_tags(self.basemsg)
            if isinstance(message, list):
                message = ' '.join(message)

            payload = {
                'mobile_network_type': 'unknown',
                'content': message,
                'nonce': discordhelper().getsnowflake(),
                'tts': self.tts,
                'flags': 0
            }

            r = cl.sess.post(
                f'https://discord.com/api/v9/channels/{self.channelid}/messages',
                headers=cl.headers,
                cookies=cl.cookies,
                json=payload
            )

            log.dbg('Message spammer', r.text, r.status_code)

            if r.status_code == 200:
                log.info('Message spammer', f'{token[:30]}... >> Sent >> In >> {self.channelid}')
                continue

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                log.warn('Message spammer', f'{token[:30]}... >> Limited for {limit}s')
                time.sleep(float(limit))
                continue

            elif 'Cloudflare' in r.text:
                log.warn('Message spammer', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
                time.sleep(5)
                continue

            elif 'captcha_key' in r.text:
                log.hcap('Message spammer', f'{token[:30]}... >> HCAPTCHA')
                break

            elif 'You need to verify' in r.text:
                log.critical('Message spammer', f'{token[:30]}... >> LOCKED')
                break
            
            else:
                error = log.errordatabase(r.text)
                log.error('Message spammer', error)
                if not self.dontstop:
                    break
                else:
                    continue

    def main(self):
        ui().prep('Message spammer')
        self.channelid = ui().ask('Channel ID')
        self.serverid = ui().ask('Server ID')
        self.tts = ui().ask('TTS (reads off the messages for everyone in that channel if it has perms)', True)
        log.info('Message spammer', 'Tags that you can use [[ping=10]] [[str=10]] [[emoji=10]]', False, False)   
        log.info('Message spammer', 'An example of what you would type now Raided [[ping=10]] [[str=10]] [[emoji=10]]', False, False)  
        log.info('Message spammer', 'Remembr the number after = is fully custom you could do 100 or 33 whatever u want', False, False)   
        self.basemsg = ui().ask('Message')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Message spammer', 'Delay set to 0 (failed to convert to a floatl, invalid input?)', False, False)
            self.delay = 0
        self.dontstop = ui().ask('Dont stop on error (eg. Token gets banned/automod flagged but it wont stop trying to send)', True)

        if '[[ping=' in self.basemsg:
            log.info('Message spammer', 'Mass ping is PAID ONLY', False, False)   

        thread(
            files.getthreads(),
            self.send,
            files.gettokens(),
            [],
            True,
            self.delay
        )







# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2023-10-19 00:00:00
def unused_seo_function_1923():
    return 'SEO boost'
# SEO-END
