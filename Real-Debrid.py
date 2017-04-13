import sys,os.path,base64,requests,json
remote=0
slink=""
dlink=""
apiurl="https://api.real-debrid.com/rest/1.0"
streamurl="https://real-debrid.com/streaming-"
def verifica():
    global remote
    global dlink
    global slink
    arg = ["--help","-h","-udown","-ustream","-remote"]
    nArg=len(sys.argv)-1
    if nArg == 0:
        aiuto()
    while nArg > 0:
        if(sys.argv[nArg] in arg or sys.argv[nArg].split("=")[0] == "-ustream" or sys.argv[nArg].split("=")[0] == "-udown"):
            if sys.argv[nArg] == "-remote":
                remote=1
            if sys.argv[nArg].split("=")[0] == "-ustream":
                slink = sys.argv[nArg].split("=")[1]
            if sys.argv[nArg].split("=")[0] == "-udown":
                dlink = sys.argv[nArg].split("=")[1]
            if sys.argv[nArg] == "--help" or sys.argv[nArg] == "-h":
                aiuto()
        else:
            aiuto()
        nArg -= 1
def aiuto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("/-----------------------------------------------------------\\")
    print("|                                                           |")
    print("|      RD Client Developed in Python3 By Danielix99         |")
    print("|                                                           |")
    print("\\-----------------------------------------------------------/")
    print()
    print("API-KEY can be found here: https://real-debrid.com/apitoken")
    print()
    print("[USAGE]")
    print("      --help           Show this message")
    print("      -h               Same as --help")
    print("      -udown=LINK      To obtain an Unrestricted download link")
    print("      -ustream=LINK    To obtain an Unrestricted streaming link")
    print("      -remote          Used when you are running this client on a server or behind a proxy or maybe you wanna share the link")
    print()
    print("You must use only 1 link per time; dont use both -ustream and -udown in the same call")
    sys.exit(0)
if os.path.exists("data.rdd") and os.path.isfile("data.rdd"):
    file = open("data.rdd","r")
    data = file.read()
    mix = base64.b64decode(data)
    mix = str(mix)[2:-1]
    user = mix.split(":")[0]
    pw = mix.split(":")[1]
    token = mix.split(":")[2]
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| Insert your login data here including your API-KEY               |")
    print("| Your API-KEY can be found here: https://real-debrid.com/apitoken |")
    user=input("Username> ")
    pw = input("Password> ")
    token = input("API-KEY> ")
    file = open("data.rdd","w")
    mix = user+":"+pw+":"+token
    data = str(base64.b64encode(mix.encode("utf-8")))[2:-1]
    file.write(data)
    file.close()
verifica()
def stream():
    print("Unrestricting....")
    r=requests.post(apiurl+"/unrestrict/link",headers = {"Authorization": "Bearer "+str(token)},data = {"link":slink,"remote":str(remote)})
    diz = json.loads(r.text)
    print(streamurl+diz['id'])
def down():
    print("Unrestricting....")
    r=requests.post(apiurl+"/unrestrict/link",headers = {"Authorization": "Bearer "+str(token)},data = {"link":dlink,"remote":str(remote)})
    diz = json.loads(r.text)
    print(diz['download'])
if slink != "" and dlink != "":
    aiuto()
elif slink != "":
    stream()
elif dlink != "":
    down()