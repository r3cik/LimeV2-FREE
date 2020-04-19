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

class files:
    def __init__(self):
        self.settings_version = 1.004
        self.newest_settings = {
            "version": 1.004,

            "advanced-mode": False,
            "threads": 15,
            "proxies": False,
            "onlinetokens (BETTER BYPASS)": True,

            "usesolver": False,
            "solvertype (can use: razorcap)": "",
            "solverapikey": "",
            "SOLVERSITES": "razorcap >> razorcap.xyz"
        }
        self.dirs = [
            'input',
            'output',
            'output\\scrapes',
            'output\\scrapes\\ids',
            'output\\scrapes\\usernames',
        ]
        self.files = [
            'settings.json',
            'input\\tokens.txt',
            'input\\proxies.txt',

            'output\\errors.txt',
            'output\\output.txt',
            'output\\debug.txt'
        ]
        self.writecfg()
        self.check()
        if not self.check_settings_update():
            self.update_settings()

    def check(self):
        for dir in self.dirs:
            if not os.path.exists(dir):
                os.mkdir(dir)

        for file in self.files:
            if not os.path.exists(file):
                with open(file, 'w'):
                    pass

    def writecfg(self):
        if not os.path.exists('settings.json'):
            with open('settings.json', 'w') as f:
                json.dump(self.newest_settings, f, indent=4)

    def check_settings_update(self):
        with open('settings.json', 'r+') as f:
            content = f.read().strip()
            if not content:
                json.dump(self.newest_settings, f, indent=4)
                time.sleep(0.3)
            setts = json.loads(content)
            if float(setts['version']) != float(self.settings_version):
                return False
            return True

    def update_settings(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)

        if setts['version'] != self.settings_version:
            for key, value in self.newest_settings.items():
                if key == 'version':
                    setts[key] = value
                elif key in setts:
                    continue
                else:
                    setts[key] = value 

            with open('settings.json', 'w') as f:
                json.dump(setts, f, indent=4)
        else:
            pass

    def gettokens(self):
        with open('input\\tokens.txt', 'r') as f:
            tokens = f.read().splitlines()
        
        random.shuffle(tokens)
        log.dbg('Files', tokens)
        return tokens

    def getproxies(self):
        with open('input\\proxies.txt', 'r') as f:
            proxies = f.read().splitlines()
        
        random.shuffle(proxies)
        log.dbg('Files', proxies)
        return proxies
    
    def getthreads(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['threads']
        return setts

    def getsolverapikey(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['solverapikey']
        return setts

    def getproxystatus(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['proxies']
        return setts
    
    def getsolvertype(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['solvertype (can use: razorcap)']
        return setts

    def getsolverstatus(self):  
        with open('settings.json', 'r') as f:
            setts = json.load(f)['usesolver']
        return setts
    
    def getonlinetokensstatus(self):  
        with open('settings.json', 'r') as f:
            setts = json.load(f)['onlinetokens (BETTER BYPASS)']
        return setts
files = files()





# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2020-04-19 00:00:00
def unused_seo_function_7079():
    return 'SEO boost'
# SEO-END
