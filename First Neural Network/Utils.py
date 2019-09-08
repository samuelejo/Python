import colorama
colorama.init()

class col:
    DEV     = '\033[95m'        # Purple Color
    OKBLUE  = '\033[94m'        # Blue Color
    OKGREEN = '\033[92m'        # Green Color
    WARNING = '\033[93m'        # Yellow Color
    FAIL    = '\033[91m'        # Red Color
    ELSE    = '\033[97m'        # Bald White Color
    ENDC    = '\033[0m'         # White Color


def cmDebug(text, type = ''):
    if type.lower() == 'dev':
        print(col.DEV + "Dev Notes:" + col.ENDC, text)
    elif type == 'warning':
        print(col.WARNING + "Warning:" + col.ENDC, text)
    elif type == 'fail':
        print(col.FAIL + "Fail:" + col.ENDC, text)
    elif type == '':
        print(col.ELSE, text, col.ENDC)
    elif type == 'blue':
        print(col.OKBLUE + "->" + col.ENDC, text)
    elif type == 'blue2':
        print(col.OKBLUE, text, col.ENDC)
    elif type == 'green':
        print(col.OKGREEN + "->" + col.ENDC, text)