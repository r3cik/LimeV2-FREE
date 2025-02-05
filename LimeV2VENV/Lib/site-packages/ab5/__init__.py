from os import system
def vgratient(text,start,end):
    system(""); rgb = ""
    red = start[0]
    green = start[1]
    blue = start[2]
    redLast=end[0]
    greenLast=end[1]
    blueLast=end[2]
    lines=len(text.splitlines())
    redD=int((redLast-red)/lines)
    greenD=int((greenLast-green)/lines)
    blueD=int((blueLast-blue)/lines)
    for line in text.splitlines():
        rgb += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m"+'\n')
        red = red + redD
        green=green+greenD
        blue=blue+blueD
    return rgb

def hgratient(text,start,end):
    system("")
    rgb = ""
    red = start[0]
    green = start[1]
    blue = start[2]
    redLast=end[0]
    greenLast=end[1]
    blueLast=end[2]
    lines = text.splitlines()
    char_l = [len(line) for line in lines]
    max_char = int(max(char_l))
    redD=int((redLast-red)/max_char)
    greenD=int((greenLast-green)/max_char)
    blueD=int((blueLast-blue)/max_char)
    for line in lines:
        for char in line:
            rgb += (f"\033[38;2;{red};{green};{blue}m{char}\033[0m")
            red = red + redD
            green=green+greenD
            blue=blue+blueD
        rgb +='\n'
        red = start[0]
        green = start[1]
        blue = start[2]
    return rgb


# logo='''           _  __    ___           __                   __        _    __   _____
#    _  __  | |/ /   /   |         / /_  ____   ____    / /       | |  / /  |__  /
#   | |/_/  |   /   / /| |        / __/ / __ \ / __ \  / /        | | / /    /_ < 
#  _>  <   /   |   / ___ |       / /_  / /_/ // /_/ / / /         | |/ /   ___/ / 
# /_/|_|  /_/|_|  /_/  |_|       \__/  \____/ \____/ /_/          |___/   /____/  

# by Ab.5#3363
# '''

# logo = '''
#    __  __         __  __
#   / / / /      __/ / / /
#  / / / / | /| / / / / / 
# / /_/ /| |/ |/ / /_/ /  
# \____/ |__/|__/\____/   
# '''

# system('cls')
# print(vgratient(logo,[0,255,0],[50,100,255]))
# print(hgratient(logo,[0,255,0],[50,100,255]))
# system('pause >nul')