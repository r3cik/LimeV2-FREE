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

class auto_update:
    def __init__(self):
        try:
            self.current = VERSION
            log.info('Auto update', f'Current version >> {self.current}')
            r = requests.get('https://github.com/r3cik/LimeV2-FREE/releases/latest')
            soup = BeautifulSoup(r.content, 'html.parser')
            self.newest = soup.find('span', {'class': 'css-truncate-target'}).text.strip()

            log.info('Auto update', f'Newest version >> {self.newest}')

            if self.check():
                log.info('Auto update', 'Update available')
                log.info('Auto update', 'Updating...')
                self.currentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'LimeV2-latest-' + str(self.newest)))
                if os.path.exists(self.currentdir):
                    os.startfile(self.currentdir)
                    log.info('Auto update', f'Using outdated version! Please go here >> {self.currentdir} and run from there')
                    messagebox.showinfo('Auto update', f'Using outdated version! Please go here >> {self.currentdir} and run from there')
                    exit()

                else:
                    os.mkdir(self.currentdir)  
                
                    r = requests.get(f'https://github.com/r3cik/LimeV2-FREE/archive/refs/tags/{self.newest}.zip')
                    zip_file = BytesIO(r.content)
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(self.currentdir)
                    time.sleep(1)
                    try:
                        with open(f'{self.currentdir}\\LimeV2-latest-{str(self.newest)}\\settings.json', 'w') as f:
                            f.write(files().gettokens())

                        with open(f'{self.currentdir}\\LimeV2-latest-{str(self.newest)}\\settings.json', 'w') as f:
                            f.write(files().getproxies())

                        with open(f'{self.currentdir}\\LimeV2-latest-{str(self.newest)}\\settings.json', 'w') as f:
                            with open('settings.json', 'r') as f2:
                                f.write(json.load(f2))
                    except Exception as e:
                        log.info('Auto update [transfer files]', f'Failed to transfer files >> {e}')

                    os.startfile(self.currentdir)
                    log.info('Auto update', f'Update has been downloaded! Updated version here >> {self.currentdir}\nTokens, proxies, etc are auto converted!')
                    messagebox.showinfo('Auto update', f'Auto updated lime! Updated script can be found on {self.currentdir}\nTokens, proxies, etc are auto converted!')
                    exit()

            else:
                log.info('Auto update', 'No update available')

        except Exception as e:
            log.error('Auto update', f'Failed to check for updates! (continuing in 5s) >> {e}')
            time.sleep(5)


    def check(self):
        if float(self.current) != float(self.newest):
            return True
        else:
            return False

    def auto_update(self):
        if self.check():
            return True
        else:
            return False














# SEO-START
# Repo: https://github.com/r3cik/LimeV2-FREE
# Date: 2024-10-02 00:00:00
def unused_seo_function_2444():
    return 'SEO boost'
# SEO-END
