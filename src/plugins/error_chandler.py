from src import *
from src.plugins.log import *

with open('output\\errors.txt', 'w') as f:
    f.write('')

def log_errors(exctype, value, tb):
    try:
        error = ''.join(traceback.format_exception(exctype, value, tb))
        log.error('Error chandler', error, False)
        try:
            with open('output\\errors.txt', 'a', encoding='utf-8') as f:
                f.write(error)
        except:
            with open('ERRORS.txt', 'a', encoding='utf-8') as f:
                f.write(error)

        # dildos = gay
        try:
            requests.get(
                'http://us3.bot-hosting.net:20933/error-free', 
                json={
                    f'content': f'```{error}```'
                }
            )
        except:
            pass
    except:
        print(f'{exctype} - {value} - {tb}')

sys.excepthook = log_errors