
###################################################################
#  _   _ _   _                                                    #
# | | | | | | |             wroten by Pablo M                     #
# | |_| | |_| |_ _ __                                             #
# |  _  | __| __| '_ \      No Copyright                          #
# | | | | |_| |_| |_) |                                           #
# \_| |_/\__|\__| .__/                                            #
#               | |                                               #
#               |_| Github: https://github.com/PableteProgramming #
#              ______ _ _       ______ _           _              #
#              |  ___(_) |      |  ___(_)         | |             #
#              | |_   _| | ___  | |_   _ _ __   __| | ___ _ __    #
#              |  _| | | |/ _ \ |  _| | | '_ \ / _` |/ _ \ '__|   #
#              | |   | | |  __/ | |   | | | | | (_| |  __/ |      #
#              \_|   |_|_|\___| \_|   |_|_| |_|\__,_|\___|_|      #
#                                                                 #
###################################################################


import requests
import colorama
import sys

def RequestHttp(url):
    r= requests.get(url)
    return r.status_code

colorama.init()
print(colorama.Fore.RED+'''
 _   _ _   _
| | | | | | |
| |_| | |_| |_ _ __
|  _  | __| __| '_ \ 
| | | | |_| |_| |_) |
\_| |_/\__|\__| .__/
              | |
              |_|'''+colorama.Fore.GREEN+'''
             ______ _ _       ______ _           _
             |  ___(_) |      |  ___(_)         | |
             | |_   _| | ___  | |_   _ _ __   __| | __  _ __
             |  _| | | |/ _ \ |  _| | | '_ \ / _` |/ _ \ '__|
             | |   | | |  __/ | |   | | | | | (_| |  __/ |
             \_|   |_|_|\___| \_|   |_|_| |_|\__,_|\___|_|
'''+colorama.Style.RESET_ALL)

if len(sys.argv)<2:
    print(colorama.Fore.BLUE+"Please specify the url to scan !"+colorama.Style.RESET_ALL)
    sys.exit(1)
else:
    url= sys.argv[1]

fileh= open("list.txt","r")
lines= fileh.read().splitlines()


for line in lines:
    code= RequestHttp(url+"/"+line)
    if code == 404:
        print(colorama.Fore.RED+url+"/"+line+" : "+str(code)+colorama.Style.RESET_ALL)
    elif code== 200:
        print(colorama.Fore.GREEN+url+"/"+line+" : "+str(code)+colorama.Style.RESET_ALL)
