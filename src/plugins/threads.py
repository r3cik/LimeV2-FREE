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