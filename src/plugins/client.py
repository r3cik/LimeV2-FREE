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
from src.plugins.files import *

class prep:
    # THIS IS ONLY THE BASE FOR CLIENT INFO NO FULL CLIENT BUILDER IN FREE SKIDDIES
    # THIS IS ONLY THE BASE FOR CLIENT INFO NO FULL CLIENT BUILDER IN FREE SKIDDIES
    # THIS IS ONLY THE BASE FOR CLIENT INFO NO FULL CLIENT BUILDER IN FREE SKIDDIES

    def __init__(self):
        log.info('Client', f'Getting client info...')
        self.identifier = 'chrome_120'
        log.info('Client', f'Getting client info...')
        self.sess = tls_client.Session(
            client_identifier=self.identifier,
            random_tls_extension_order=True,
        )

        self.headers = {}
        log.info('Client', f'Getting user-agent and xsuper')
        r = requests.get('https://raw.githubusercontent.com/r3cik/discord-api/refs/heads/main/latest.json').json()
        self.xsup = r['X-Super-Properties']
        self.ua = r['User-Agent']
        log.info('Client', f'Got user-agent >> {self.ua[:5]}... and xsuper >> {self.xsup[:5]}...')
        self.reffrer = 'https://discord.com/channels/@me'
        log.info('Client', f'Refferer >> {self.reffrer}')
        self.xtimezone = 'Europe/Warsaw'
        log.info('Client', f'Xtimezone >> {self.xtimezone}')

        self.cookies = {}
        self.cookies_renew()
        log.info('Client', f'Renewed discord info')

        self.headers_form()
        log.info('Client', f'Formed headers')

    def cookies_renew(self):
        r = self.sess.get(
            'https://discord.com',
            headers=self.headers
        )

        cookies_ = r.cookies.get_dict()
        self.cookies['__dcfduid'] = cookies_.get('__dcfduid')
        self.cookies['__sdcfduid'] = cookies_.get('__sdcfduid')
        self.cookies['_cfuvid'] = cookies_.get('_cfuvid')
        self.cookies['locale'] = 'en-US'
        self.cookies['__cfruid'] = cookies_.get('__cfruid')

    def headers_form(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-GB,pl;q=0.9',
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com',
            'Referer': self.reffrer,
            'Priority': 'u=1, i',
            'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': self.ua,
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': self.xtimezone,
            'X-Super-Properties': self.xsup
        }

prep = prep()

class client:
    def __init__(self, token=None):
        self.token = token
        self.proxy = None

        self.sess = tls_client.Session(
            client_identifier=prep.identifier,
            random_tls_extension_order=True,
        )

        self.headers = prep.headers
        self.cookies = prep.cookies
        self.xsup = prep.xsup
        self.ua = prep.ua

        if files.getproxystatus():
            self.proxy = random.choice(files.getproxies())
            self.sess.proxies = {
                'http': 'http://' + self.proxy,
                'https': 'https://' + self.proxy
            }











# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2025-02-05 12:58:42
def unused_seo_function_6925():
    return 'SEO boost'
# SEO-END
