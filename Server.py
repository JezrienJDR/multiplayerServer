# Server script (w/matchMaking)

import request
import json
import socket
import sys
from _thread import *
import threading
from datetime import datetime

getPlayerById = "https://fv59sknmtk.execute-api.us-east-1.amazonaws.com/default/getPlayerByID"
getAllPlayers = "https://8hypg89sb5.execute-api.us-east-1.amazonaws.com/Dev/getPlayers"
addPlayerData = "https://pfd0ora1uk.execute-api.us-east-1.amazonaws.com/default/addPlayerData"
deletePlayer = "https://2su9zrko91.execute-api.us-east-1.amazonaws.com/default/deletePlayer"

def getPlayer(searchID):

    queryURL = getPlayerById + "?PID=" + searchID

    response = requests.get(queryURL)
    responseJson = json.loads(response)

    return responseJson['rating']

def getPlayerList():

    response = requests.get(getAllPlayers)
    responseJson = json.loads(response)

    for item in responseJson:
        fullPlayerList[item['PID']]['rating'] = item['rating']

def updatePlayer(PID, rating):

    queryURL = addPlayerData + "?PID=" + PID + "&" + "rating=" + rating
    response = requests.get(queryURL)

def deletePlayer(PID):

    queryURL = deletePlayer + "?PID=" + PID
    response = requests.get(queryURL)


clients_lock = threading.Lock()
connected = 0

class Player:
    PID = ""
    rating = ""

class Game:
    players = {}

fullPlayerList = {}
clients = {}
clientsNotInGame = {}
gameList = {}



def connectionLoop(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        data = str(data)
        if addr in clients:
            clients[add]['lastBeat'] = datetime.now()
        else:
            clients[addr] = {}
            clients[addr]['lastBeat'] = datetime.now()
            
            m = json.loads(data)

            id = m['PID']

            if id in fullPlayerList.keys():
                clients[addr]['rating'] = fullPlayerList[id]['rating']
                clients[addr]['PID'] = id
            else:

        
            if m['PID'] == "NOID":
                for x in range(100):
                    if                     

            clients[addr]['PID'] = m['PID']
            clients[addr]['rating'] = m['rating']

            clientsNotInGame[addr] = clients[addr]




def matchMaking(sock):


def gameLoop(sock):


def cleanClients(sock):

def setup():
    getPlayerList()


def main():
    print("Hello World! SERVER ONLINE!")

    Host = ''	
    Port = 12345	

    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    s.bind(('', Port))

    setup()

    start_new_thread(gameLoop, (s,))
    start_new_thread(matchMacking, (s,))
    start_new_thread(connectionLoop, (s,))
    start_new_thread(cleanClients, (s,))
    while True:
        time.sleep(1)

    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()




if __name__ == "__main__":
    main()