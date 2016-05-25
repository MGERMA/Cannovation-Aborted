import socket
import select

###################### PARAMETRAGE HOST ##############

Host = '127.0.0.1'
Port = 80
Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Sock.bind((Host,Port))

#Host = '172.21.30.41'
#Port = 80                   LYCEE POSTE P6
#Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Sock.bind((Host,Port))


#Host = '127.0.0.1'
      #Port = 234              MAISON
#Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Sock.bind((Host,Port))

######################

Sock.listen(5)
print("Le serveur écoute à présent sur le port {}".format(Port))
serveur_on = True
clients_ok= []
nb_clients = int(0)
while serveur_on:
    connexions_demandees, wlist, xlist = select.select([Sock],[], [], 0.05)
    for connexion in connexions_demandees:
        client, adresse = connexion.accept()
        clients_ok.append(client)
        nb_clients += 1
       # hello_mess=str("Clients connectés: ")
       # client.send(bytes(hello_mess,"utf-8"),nb_clients)
        

    clients_att = []
    try:
        clients_att, wlist, xlist = select.select(clients_ok,[], [], 0.05)
    except select.error:
        pass
    else:
        # liste des clients à lire
        for client in clients_att:
            # Client est de type socket
            try:
                msg = client.recv(1024)
            except socket.error:
                continue
            # Peut planter si le message contient des caractères spéciaux
            msg = msg.decode()
            print("Reçu {}".format(msg))
            msgs=bytes(msg,"utf-8")
            for client in clients_ok:
                try:
                    client.send(msgs)
                except socket.error:
                    continue
                if msg == "close":
                    serveur_on = False

print("Fermeture des connexions")
for client in clients_ok:
        client.close()

        

Sock.close()


