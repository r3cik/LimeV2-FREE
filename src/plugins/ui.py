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
from src.plugins.files import *

class ui:
    def __init__(self):
        self.size = os.get_terminal_size().columns
        self.font = 'dos_rebel'

    def makebanner(self, text):
        banner = pyfiglet.figlet_format(text, font=self.font, width=self.size)
        banner = banner.rstrip('\n')
        banner_lines = banner.split('\n')
        banner_lines = banner_lines[:-3]
        max_line_length = max(len(line) for line in banner_lines)
        spaces_to_center = (self.size - max_line_length) // 2
        centered_banner = '\n'.join([line.rjust(len(line) + spaces_to_center) for line in banner_lines])
        print('\n')
        print(ab5.vgratient(centered_banner, co.gradient1, co.gradient2))

    def banner(self):
        self.makebanner('Lime V2')
        print(ab5.vgratient('FREE VERSON - BUY PAID ON DISCORD.GG/FLOODING - GITHUB.COM/r3cik/LimeV2-FREE'.center(self.size), co.gradient1, co.gradient2))

    def stats(self):
        stats = f'Tokens {len(files.gettokens())}  |  {len(files.getproxies())} Proxies'.center(self.size)
        print(ab5.vgratient(stats, co.gradient1, co.gradient2))

    def menu(self):
        menu = f"""
{'01 Joiner (F)      06 Message spam (F) 11 Checker  (F)    16 Onboarding      21 Mass Dm         26 User scraper      '.center(self.size)}
{'02 Leaver (F)      07 Threads spam     12 Avatar changer  17 Reaction (F)    22 Spam call       27 ID scraper        '.center(self.size)}
{'03 Is in server (F)08 Threads2 spam    13 Bio changer     18 Rules           23 Mass friend     28 Booster           '.center(self.size)}
{'04 Anti ban        09 Poll spam        14 Disp changer (F)19 Button          24 Mass ticket     29 Token nuke        '.center(self.size)}
{'05 Nick changer    10 Chat crasher     15 Pron changer    20 Restorecord     25 React bomb      30 Combo to token (F)'.center(self.size)}
{'>> Next page'.center(self.size)}
"""
            
        print(ab5.vgratient(menu, co.gradient1, co.gradient2))

    def menu2(self):
        menu2 = f"""
{'31 Mass send       06 Message spam     11 Checker         16 Onboarding      21 Mass Dm         26 User scraper  '.center(self.size)}
{'32 Token fucker    07 Threads spam     12 Avatar changer  17 Reaction        22 Spam call       27 ID scraper    '.center(self.size)}
{'33 Invite scraper  08 Threads2 spam    13 Bio changer     18 Rules           23 Mass friend     28 Booster       '.center(self.size)}
{'34 Msg listener    09 Poll spam        14 Disp changer    19 Button          24 Mass ticket     29 Token nuke    '.center(self.size)}
{'35 None            10 Chat crasher     15 Pron changer    20 Restorecord     25 React bomb      30 Combo to token'.center(self.size)}
{'<< Back'.center(self.size)}
"""
        
        print(ab5.vgratient(menu2, co.gradient1, co.gradient2))

    def cls(self):
        os.system('cls')
    
    def title(self, x):
        os.system(f'title Lime V2 FREE - github.com/r3cik/LimeV2-FREE - {x}')

    def prep(self, module):
        self.cls()
        self.title(module)
        #self.banner()
        self.makebanner(module)

    def ask(self, x, yn=False):
        x = ab5.hgratient(f'[{x}]', co.gradient1, co.gradient2).strip()
        if yn:
            x = input(f'{x} (y/n) >> {S.RESET_ALL}')
            if x in ['y', 'Y', 'yes', 'Yes', 'YES']:
                return True
            else:
                return False
        else:
            return input(f'{x} >> {S.RESET_ALL}')
    
    def make_menu(self, options):
        for index, option in enumerate(options, 1):
            indx = ab5.hgratient(f'[{index:02d}]', co.gradient1, co.gradient2).strip()
            opt = ab5.hgratient(f'[{option}]', co.gradient1, co.gradient2).strip()
            print(f'{indx} >> {opt}{S.RESET_ALL}')

        print('\n')
























