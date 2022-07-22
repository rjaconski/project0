from abc import ABC, abstractmethod


class Track(ABC):
    def __init__(self, laps, turns, straight):
        self._laps = int(laps)
        self._turns = int(turns)
        self._straight = int(straight)
    
    def setTrack(self,laps,turns,straight):
        self._laps = int(laps)
        self._turns = int(turns)
        self._straight = int(straight)
        
class ovalTrack(Track):
    
    
    def setTrack():
        return([4,4,4])

class roadCourse(Track):
    def setTrack():
       
        return([2,6,8])
      
        
    
class drag(Track):
    def setTrack():
        
        return([1,4,0])
    