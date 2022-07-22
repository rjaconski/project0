from abc import ABC, abstractmethod
import random


class Car(ABC):
    def __init__(self, speed):
        self._speed = str(speed)
    
    @abstractmethod            
    def start(self):
        pass
        
    @abstractmethod
    def straight(self):
        pass
        
    @abstractmethod
    def turn(self):
        pass
        
    
class Awd(Car):
    def turn(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points
    
    def straight(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points
        

class Fwd(Car):
        
    def start(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points
        
    def straight(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points

class Rwd(Car):
    
    def start(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points
    
    def turn(speed):
        if speed  == "1":
            points = 1
        elif speed  == "2":
            points = chanceRoll(50)
        else:
            pass
        return points
    
def chanceRoll(percentChance):
    if random.randint(1,100) < percentChance:
        return 2
    else:
        return 0   