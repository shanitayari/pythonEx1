from dotenv import load_dotenv
import os
class Car:
    def __init__(self):
        """
        create new car and initialize it
        name: shani
        date: 22.1.23
        :param: none
        :return: none
        """
        load_dotenv()
        self.gear=0
        self.money=int(os.getenv("moneyInit"))
        self.fuel=int(os.getenv("fuelInit"))
        self.isStart=False
        self.isDrive=False
        self.fuelConsumption=int(os.getenv("fuelConsumption"))
        self.fuelCapacity=int(os.getenv("fuelCapacity"))
    def gearUp(self):
        """gear up in car"""
        if not self.isStart:
            raise Exception(os.getenv("gearStopError"))
        if self.gear==int(os.getenv("maxGear")):
            raise Exception(os.getenv("gearMaxError"))
        self.gear+=1
        if self.gear==1:
            self.isDrive=True
    def gearDown(self):
        """gear down in car"""
        if self.gear==0:
            raise Exception(os.getenv("gearMinError"))
        self.gear-=1
        if self.gear==0:
            self.isDrive=False
    def start(self):
        """start the car"""
        if self.isDrive:
            raise Exception(os.getenv("startError"))
        self.isStart=True
    def stop(self):
        """stop the car"""
        self.isStart=False
        self.isDrive=False
        self.gear=0
    def drive(self,km):
        """drive x km"""
        if not self.isStart:
            raise Exception(os.getenv("driveStopError"))
        if km<0:
            raise Exception(os.getenv("kmError"))
        if self.fuel*self.fuelConsumption<km:
            raise Exception(os.getenv("fuelError"))
        self.fuel-=km/self.fuelConsumption
    def toFuel(self):
        """fuel the car"""
        price=(self.fuelCapacity-self.fuel)*int(os.getenv("fuelPrice"))
        if price>self.money:
            raise Exception(os.getenv("moneyError"))
        self.fuel=self.fuelCapacity
        self.money-=price
    def getGear(self):
        """get current gear"""
        return self.gear
    def getSpeed(self):
        """get current speed"""
        return self.gear*int(os.getenv("gear"))
    def getMoney(self):
        """get current money amount"""
        return self.money
    def getFuel(self):
        """get current fuel amount"""
        return self.fuel
    def getIsStart(self):
        """get if car started"""
        return self.isStart
    def getIsDrive(self):
        """get if its driving state"""
        return self.isDrive