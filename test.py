import os, time, ctypes, threading, base64
os.system('title Lime V2')
def _(): 
    start=time.time()
    while time.time()-start<int(base64.b32decode('GU======'.encode()).decode()):
        buf=ctypes.create_unicode_buffer(255);ctypes.windll.kernel32.GetConsoleTitleW(buf,base64.b32decode('GI2TK==='.encode()).decode())
        time.sleep(int(base64.b32decode('GYYA===='.encode()).decode()))
        if all([ord(x)^0xF!=ord(c)for x,c in zip(bytes.fromhex('4C696D65205632').decode(),buf.value)]):print(bytes.fromhex('496D6167696E6520736B696464696E67206C6F6C20646973636F72642E67672F666C6F6F64696E67').decode())
    os._exit(base64.b32decode('GA======'.encode()).decode())
threading.Thread(target=_, daemon=True).start()
time.sleep(100)