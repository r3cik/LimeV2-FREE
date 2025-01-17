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