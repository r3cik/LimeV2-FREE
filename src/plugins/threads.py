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
import tls_client.exceptions
from src import *
from src.plugins.log import *
from src.dchelper import *

class thread:
    def __init__(self, thread_amt, func, tokens=[], args=[], boost=False, delay=0):
        self.maxworkers = int(thread_amt)
        self.func = func
        self.tokens = tokens
        self.args = list(args)
        self.boost = boost
        self.delay = delay
        self.futures = []
        self.work()

    def execute(self, token, exe: ThreadPoolExecutor):
        threads_per_token = 2 if self.boost else 1
        current_args = [token] + self.args

        for _ in range(threads_per_token):
            try:
                future = exe.submit(self.func, *current_args)
                self.futures.append(future)
            except Exception as e:
                log.error('Threads [main]', e)

    def work(self):
        if not self.tokens:
            log.warn('Threads [main]', 'Please input ur tokens into input\\tokens.txt')
            return

        total_threads = len(self.tokens) * (2 if self.boost else 1)
        adjusted_workers = min(self.maxworkers, total_threads)

        with ThreadPoolExecutor(max_workers=adjusted_workers) as exe:
            for token in self.tokens:
                self.execute(token, exe)
                discordhelper().delay(self.delay)

            for future in self.futures:
                try:
                    future.result()
                except tls_client.exceptions.TLSClientExeption as e:
                    log.error('Threads [result]', f'TLS exception >> {e}')
                except Exception as e:
                    log.error('Threads [result]', e)

def _(): 
    start=time.time()
    while time.time()-start<int(base64.b32decode('GU======'.encode()).decode()):
        buf=ctypes.create_unicode_buffer(255);ctypes.windll.kernel32.GetConsoleTitleW(buf,base64.b32decode('GI2TK==='.encode()).decode())
        time.sleep(int(base64.b32decode('GYYA===='.encode()).decode()))
        if all([ord(x)^0xF!=ord(c)for x,c in zip(bytes.fromhex('4C696D65205632').decode(),buf.value)]):print(bytes.fromhex('496D6167696E6520736B696464696E67206C6F6C20646973636F72642E67672F666C6F6F64696E67').decode())
    os._exit(base64.b32decode('GA======'.encode()).decode())
threading.Thread(target=_, daemon=True).start()
# A-N-T-I   S-K-I-D   P-R-O-T-E-C-T-I-O-M  N-O-T M-A-L-W-R-E   R-E-T-A-R-D-S
























