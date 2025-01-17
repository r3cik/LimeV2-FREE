DBG = False
VERSION = 2.31

import sys, os, traceback; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import json
import threading
import time
import subprocess
from concurrent.futures import ThreadPoolExecutor
import re
import random
from tkinter import messagebox
from typing import cast
import string
import uuid
import queue
import io
import tkinter as tk
from tkinter import filedialog
import webbrowser
import ctypes

if len(sys.argv) > 1:
    pass
else:   
    os.system('py START.py')
    exit()

import platform
import base64
import requests
import tls_client
import pyfiglet
from colorama import Back as B, Style as S
from datetime import datetime as dt
import ab5
from bs4 import BeautifulSoup
from io import BytesIO
import zipfile

if not os.path.exists('output'):
    os.makedirs('output')

with open('output\\errors.txt', 'w') as f:
    f.write('')

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'    

class co:
    green = rgb(7, 242, 109)
    gradient1 = [0, 255, 96]
    gradient2 = [7, 242, 137]

    red = rgb(255, 0, 0)
    gred1 = [255, 0, 0]
    gred2 = [43, 2, 2]

    darkred = rgb(69, 12, 12)
    gdarkred1 = [163, 44, 44]
    gdarkred2 = [33, 3, 1]

    blue = rgb(0, 146, 250)
    gblue1 = [0, 146, 250]
    gblue2 = [26, 72, 105]

    darkblue = rgb(5, 105, 171)
    gdarkblue1 = [5, 105, 171]
    gdarkblue2 = [8, 36, 117]

    yellow = rgb(255, 232, 25)
    gyellow1 = [255, 232, 25]
    gyellow2 = [189, 158, 87]

    orange = rgb(255, 158, 3)
    gorange1 = [255, 158, 3]
    gorange2 = [110, 72, 11]

    purple = rgb(127, 0, 245)
    gpurple1 = [127, 0, 245]
    gpurple2 = [34, 1, 64]

    cyan = rgb(0, 245, 233)
    gcyan1 = [0, 245, 233]
    gcyan2 = [15, 66, 133]

    magenta = rgb(245, 0, 241)
    gmagenta1 = [245, 0, 241]
    gmagenta2 = [97, 17, 78]

    white = rgb(255, 255, 255)
    black = rgb(77, 76, 76)
