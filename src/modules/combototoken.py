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
from src.plugins.threads import * 
from src.plugins.files import *

class combototoken:
    def __init__(self):
        self.serverid = None
        self.valids = []

    def convert(self):
        tokens = files.gettokens()

        with open('input\\tokens.txt', 'w') as f:
            for combo in tokens:
                if ':' in combo:
                    f.write(f'{combo.strip().split(":")[2]}\n')

    
    def main(self):
        ui().prep('Combto to token')
        self.convert()


# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2023-06-26 00:00:00
def unused_seo_function_7348():
    return 'SEO boost'
# SEO-END
