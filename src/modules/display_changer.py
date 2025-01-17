from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.dchelper import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class displaychanger:
    def __init__(self):
        self.newdisplay = None

        self.delay = 0

    def change(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        payload = {
            'global_name': self.newdisplay
        }

        r = cl.sess.patch(
            f'https://discord.com/api/v9/users/@me',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Display changer', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Display changer', f'{token[:30]}... >> Changed to >> {self.newdisplay}')

        elif 'retry_after' in r.text:
            limit = r.json().get('retry_after', 1.5)
            log.warn('Display changer', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.change(token)

        elif 'Cloudflare' in r.text:
            log.warn('Display changer', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.change(token)

        elif 'captcha_key' in r.text:
            log.hcap('Display changer', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Display changer', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Display changer', error)
    
    def main(self):
        ui().prep('Display changer')
        self.newdisplay = ui().ask('New display')
        try:
            self.delay = float(ui().ask('Delay (0 for no delay)'))
        except:
            log.info('Display changer', 'Delay set to 0 (failed to convert to a floatl, invalid input?)', False, False)
            self.delay = 0

        thread(
            files.getthreads(),
            self.change,
            files.gettokens(),
            [],
            False,
            self.delay
        )