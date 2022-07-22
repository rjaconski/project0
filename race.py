from csv import writer
import csv
import logging
import re
import random
from track import ovalTrack, drag, roadCourse
from cars import Awd, Rwd, Fwd 


def main():
    logging.basicConfig(filename="drivers.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    file1 = "playerList.csv"
    driverData = []
    player =[]
    
    print("WELCOME!\n")
    print("\t1) Start a new game?\n")
    print("\t2) Load a saved game?\n")
    print("\t3) Quit game")
    ch1 = input(">>>")
    if ch1 not in ["1", "2"]:
        logging.error("Quitting game...")
        
    if ch1 == "1":
        player = addDriver(file1)
        driverData= [player[0],int(player[1]),int(player[2]),int(player[3]),int(player[4])]
        chooseCar(file1, driverData)
        
    elif ch1 == "2":
        player = loadPlayer(file1)
        
        if player != None:
            driverData= [player[0],int(player[1]),int(player[2]),int(player[3]),int(player[4])]
            chooseCar(driverData, file1)
        else:
            logging.error("Driver data not found ending game...")
                
def newGame(driverData,file1):
    logging.info("Starting a new game...")

    print("\nStarting a new race!\n")
    chooseCar(driverData,file1)
    
def readFile(name,file1):
    with open(file1, 'r') as readFile:
        reader = csv.reader(readFile)   
        for i in reader:
            print(i[0])
            if i[0] == name:
                print("found")
                return True
            else:
                continue
    return False
    
def chooseCar(driverData, file1):

    print("\nChoose your Car Type:")
    print("\t1) AWD")
    print("\t2) RWD")
    print("\t3) FWD")
    print("\t4) Quit")
    ch1 = input(">>>")
    cars = [Awd, Rwd, Fwd]
    computer = random.choice(cars)
    print(computer)
    if ch1 == "1":
        playerCar = Awd

    elif ch1 == "2":
        playerCar = Rwd

    elif ch1 == "3":
        playerCar = Fwd

    else:
        return None
    
    chooseTrack(playerCar, computer, driverData, file1)
    
def chooseTrack(playerCar, computer, driverData, file1):
        
    print("\nChoose your track:")
    print("\t1) Oval")
    print("\t2) Road course")
    print("\t3) Dragstrip")
    track = input(">>>")
    tType = []
    
    if track == "1":
        tType = ovalTrack.setTrack()
        race(tType, playerCar, computer, driverData, file1)
    
    elif track == "2":
        tType = roadCourse.setTrack() 
        race(tType, playerCar, computer, driverData, file1)
    
    elif track == "3":
        tType = drag.setTrack()
        race(tType, playerCar, computer, driverData, file1)     
    
    else:
        return None

def loadPlayer(file1):
    driverList= []
    count = 0
    with open(file1, 'r') as c:
        readin = csv.reader(c)
        next(readin)
        for driver in readin:    
            print( str(driver[0]) + " - Wins: " + str(driver[1]) + " Loses: " +str(driver[2]) + " Ties: " + str(driver[3]) + " Total points: " + str(driver[4]))
            driverList.append(driver)
            count = count + 1
        
    if count == 0: #test to make sure csv file has driver data
            logging.error("No drivers found in csv file...")
            print("No drivers found. \nWould you like to create a driver?")
            ch2 = input("\t1) Yes\n\t2) No\n>> ")
                
            if ch2 == "1":
                return(addDriver(file1))
            else:
                return None
    else:
        logging.info("Loaded list of previous drivers..")
        
    count2 = 0
    while(True):
        ch1 = input("Choose your Driver: ")
        print(count)
        for i in driverList:
            
            if i[0] == ch1:
                return (i)
            
            elif count2 == count-1:
                logging.info("Entry error Driver not found...")
                print("Player not found choose again. Try again?")
                ch2 = input("\t1) Yes\n\t2) No\n>> ")
                
                if ch2 == "1":
                    continue
                elif ch2 == "2":
                    print("Would you like to create a new Driver?")
                    print("\t1) Yes")
                    print("\t2) No")
                    ch3 = input(">> ")
                    if ch3 == "1":
                        return(addDriver(file1))
                    else:
                        return None
                else:
                    return None
            count2 = count2 + 1
        
def addDriver(file1):
    while True:
        try:
            name = input("Driver enter your name: ")
            check = re.search(',', name) #checks if there is a (,) used in the name and gives the variable check a value if it does
            checkRepeat = readFile(name,file1)
            if check != None:#value of check is tested
                logging.error("Tried to enter a comma in name, trying again...")
                raise ValueError
            elif checkRepeat == True:
                print("Error name already exists choose another.")
                logging.error("Tried to enter a name that already exists, trying again...")
                raise ValueError
        except ValueError as ve:
            pass
            
        else:
            break
    
    driverData = [name,0,0,0,0]
    with open(file1, "a", newline='') as c:
        writeObj = writer(c)
        writeObj.writerow(driverData)
        c.close()
    return(driverData)

def updatePlayer(driverData,file1):
    count = 0
    with open(file1, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader) # csv is made into an array
        for i in lines:
            if i[0] == driverData[0]:
                lines[count] = driverData
                break
            else:
                count = count + 1
    
    with open(file1, 'w', newline = '') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    logging.info("Driver data updated...")       
        

def race(tType, playerCar, computerCar, driver, file1):
    
    print("\t\tStart your engines!")
    player1 = 0
    computer = 0
    if playerCar == Rwd or playerCar == Fwd:
        print("Race is starting how fast do you want to go?")
        print("\t1) Normal speed")
        print("\t2) Full throtal")
        speed = input(">>>")
            
        player1 = playerCar.start(speed)
                            
    elif computerCar == Rwd or computerCar == Fwd:
        computer = 1
            
    if computerCar == Awd:
        computer = 3
    if playerCar == Awd:
        player1 = 3
    print("Current Points:\n\tPlayer1:" + str(player1) + "\n\tComputer:" + str(computer) + "\n")
            
    while tType[0] > 0: # Runs through the laps
        while tType[1] > 0 or tType[2] > 0: #runs through turns and straights
            if tType[2] > 0: #checks for turns
                player1, computer = turning(playerCar, computerCar, computer, player1)
                
                tType[2] = tType[2] - 1
                
            if tType[1] > 0: #checks for straights
                
                player1, computer = straight(playerCar, computerCar, computer, player1)               
                
                tType[1] = tType[1] - 1
        tType[0] = tType[0] - 1
    print("\t\tFinal Results!!!")
    if computer > player1:
        print("The computer wins with " + str(computer) + " points.")
        print("Player1 ends with " + str(player1) + " points, better luck next time!!")

        driver[2] = int(driver[2]) + 1
            
    elif computer < player1:
        print("Congradulations the player has won with " + str(player1) + " points!!")

        driver[1] = int(driver[1]) + 1    
    else:    
        print("It's a tie both racers recieved " + str(computer) + " points!!")

        driver[3] = int(driver[3]) +1

    driver[4] = driver[4] + player1

    updatePlayer(driver,file1)

    print("\nWould you like to play again?")
    print("\t1) Yes")
    print("\t2) No")
    ch3 = input(">>")
    if ch3 == "1":
        newGame(driver, file1)
    else:
        print("Game over!\nThanks for playing!")
        logging.info("Ending the game..")
        
def turning(playerCar, computerCar, computer, player1):
    if computer < player1:
        speed2 = "2"
    elif computer >= player1:
        speed2 = "1"
    print(speed2)    
    if computerCar == Fwd:
        computer = computer + 2
    elif computerCar == Rwd:
        computer = computer + Rwd.turn(speed2)
    elif computerCar == Awd:
        computer = computer + Awd.turn(speed2)
                        
    if playerCar == Fwd:
        print("A turn is coming up!")
        player1 = player1 + 2
    elif playerCar == Rwd or playerCar == Awd:
        print("A turn is coming up how fast do you want to go?")
        print("\t1) Normal speed")
        print("\t2) Full throttle")
        speed1 = input(">>>")
        player1 = player1 + playerCar.turn(speed1)
    elif playerCar == "Awd":
        print("A turn is coming up how fast do you want to go?")                            
        print("\t1) Normal speed")
        print("\t2) Full throttle")
        speed1 = input(">>>")
        player1 = player1 + Awd.turn(speed1)
    print("Current Points:\n\tPlayer1:" + str(player1) + "\n\tComputer:" + str(computer) + "\n")
    return player1, computer


def straight(playerCar, computerCar, computer, player1):
    if computer < player1:
        speed2 = "2"
                            
    elif computer >= player1:
        speed2 = "1"
        
    if computerCar == Rwd:
        computer = computer + 2
                            
    elif computerCar == Fwd:
        computer = computer + Fwd.straight(speed2)
                            
    elif computerCar == Awd:
        computer = computer + Awd.straight(speed2)
                        
    if playerCar == Rwd:
        print("A Straight away is coming up!")
        player1 = player1 + 2
                            
    elif playerCar == Fwd:
        print("A Straight away is coming up how fast do you want to go?")
        print("\t1) Normal speed")
        print("\t2) Full throttle")
        speed1 = input(">>>")
        player1 = player1 + Fwd.straight(speed1)
                            
    elif playerCar == Awd:
        print("A Straight away is coming up how fast do you want to go?")
        print("\t1) Normal speed")
        print("\t2) Full throttle")
        speed1 = input(">>>")
        player1 = player1 + Awd.turn(speed1)
        
    print("Current Points:\n\tPlayer1:" + str(player1) + "\n\tComputer:" + str(computer) + "\n")
    
    return player1, computer
main()