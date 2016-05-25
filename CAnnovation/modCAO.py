import socket
import easygui as eg

######################## PARAMETRAGE HOST ##########

def param():
    msg="Entrez les infos:"
    title="Parametrage du socket"
    champs=["Hote","Port","Mot de passe"]
    defaultvalues=["127.0.0.1","80",""]

    #defaultvalues=["172.21.30.31","80",""]

    valeurs_des_champs=eg.multpasswordbox(msg,title,champs,defaultvalues)


    H = valeurs_des_champs[0]
    P = int(valeurs_des_champs[1])
    return(H,P)

############################## FONCTION ENVOYER ######

def envoy(paramtuple, x):
    Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Sock.connect(paramtuple)
    
    Sock.send(str(x).encode('utf-8'))
    
############################## FONCTION RECEIVE ######
def recev(paramtuple):
    Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Sock.connect(paramtuple)
    
    rep=Sock.recv(1024)
    rep=rep.decode()
    return(rep)


