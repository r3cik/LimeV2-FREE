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

class reaction:
    def __init__(self):
        self.serverid = None
        self.channelid = None
        self.messageid = None
        self.reaction = None
        self.dodebypass = False

        self.delay = 0

    def bypass(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.put(
            f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{self.reaction}/@me?location=Message&type=0',
            headers=cl.headers,
            cookies=cl.cookies
        )

        log.dbg('Reaction', r.text, r.status_code)

        if r.status_code == 204:
            log.info('Reaction', f'{token[:30]}... >> Bypassed')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Reaction', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.bypass(token)

        elif 'Cloudflare' in r.text:
            log.warn('Reaction', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.bypass(token)

        elif 'captcha_key' in r.text:
            log.hcap('Reaction', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Reaction', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Reaction', error)
    
    def debypass(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.delete(
            f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{self.reaction}/@me?location=Message&type=0',
            headers=cl.headers,
            cookies=cl.cookies
        )
    
        log.dbg('De reaction', r.text, r.status_code)

        if r.status_code == 204:
            log.info('De reaction', f'{token[:30]}... >> De reacted')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('De reaction', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.debypass(token)

        elif 'Cloudflare' in r.text:
            log.warn('De reaction', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.bypass(token)

        elif 'captcha_key' in r.text:
            log.hcap('De reaction', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('De reaction', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('De reaction', error)

    def main(self):
        ui().prep('Reaction bypass')
        self.serverid = ui().ask('Server ID')
        self.channelid = ui().ask('Channel ID')
        self.messageid = ui().ask('Message ID')
        self.dodebypass = ui().ask('Do de bypass? (If the tokens alerdy reacted this will also first remove the rection so they get actualy verified again)', True)
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Reaction', 'Delay set to 0 (failed to convert to a floatl, invalid input?)', False, False)
            self.delay = 0

        reacts = []
        messages = discordhelper().get_messages(self.channelid, files.gettokens())
        try:
            for message in messages:
                if message['id'] == self.messageid:
                    if not message['reactions']:
                        log.info('Reaction', 'No reactions found')
                        return
                    
                    for reaction in message['reactions']:
                        emoji_name = reaction['emoji']['name']
                        count = reaction['count']
                        reacts.append((emoji_name, count))

            mn = []
            for _, (reactionname, count) in enumerate(reacts, 1):
                mn.append(f'{reactionname} - {count}')
        except Exception as e:
            log.error('Reaction', f'Failed to get reactions, none on the message? >> {e}')
            return


        ui().make_menu(mn)
        selected = int(ui().ask('Choice')) - 1
        self.reaction = reacts[selected][0]

        if self.dodebypass:
            thread(
                files.getthreads(),
                self.debypass,
                files.gettokens(),
                [],
                False,
                self.delay
            )

        time.sleep(1)

        thread(
            files.getthreads(),
            self.bypass,
            files.gettokens(),
            [],
            False,
            self.delay
        )



































