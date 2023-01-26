import unittest
from Car.car import Car
from Car.log import Log
from dotenv import load_dotenv
import os
class Test(unittest.TestCase):
    def setUp(self):
        self.car=Car()
        self.log=Log()
        load_dotenv()
    def test_gearUp(self):
        """test gear up"""
        try:
            self.car.start()
            self.car.gearUp()
            self.assertEqual(self.car.gear,1)
            self.log.printToFile("test_gearUp passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_gearUp failed "+str(assertionError))
    def test_gearUpInStop(self):
        """test gear up in stop"""
        try:
            with self.assertRaises(Exception):
                self.car.gearUp()
            self.log.printToFile("test_gearUpInStop passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_gearUpInStop failed "+str(assertionError))
    def test_gearDown(self):
        """test gear down"""
        try:
            self.car.start()
            self.car.gearUp()
            self.car.gearDown()
            self.assertEqual(self.car.gear,0)
            self.log.printToFile("test_gearDown passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_gearDown failed "+str(assertionError))
    def test_gearDownLessMin(self):
        """test gear down less than min"""
        try:
            with self.assertRaises(Exception):
                self.car.gearDown()
            self.log.printToFile("test_gearDownLessMin passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_gearDownLessMin failed "+str(assertionError))
    def test_start(self):
        """test start the car"""
        try:
            self.car.start()
            self.assertEqual(self.car.isStart,True)
            self.log.printToFile("test_start passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_start failed "+str(assertionError))
    def test_startInDrive(self):
        """test start in drive"""
        try:
            self.car.start()
            self.car.gearUp()
            with self.assertRaises(Exception):
                self.car.start()
            self.log.printToFile("test_startInDrive passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_startInDrive failed "+str(assertionError))
    def test_stop(self):
        """test stop the car"""
        try:
            self.car.stop()
            self.assertEqual(self.car.isStart,False)
            self.assertEqual(self.car.isDrive,False)
            self.assertEqual(self.car.gear,0)
            self.log.printToFile("test_stop passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_stop failed "+str(assertionError))
    def test_drive(self):
        """test drive x km"""
        try:
            self.car.start()
            self.car.drive(5)
            self.assertEqual(self.car.fuel,int(os.getenv("fuelInit"))-5/self.car.fuelConsumption)
            self.log.printToFile("test_drive passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_drive failed "+str(assertionError))
    def test_driveInStop(self):
        """test drive in stop"""
        try:
            with self.assertRaises(Exception):
                self.car.drive(5)
            self.log.printToFile("test_driveInStop passed")
        except AssertionError as assertionError:
            self.log.printToFile("test_driveInStop failed "+str(assertionError))
if __name__=='__main__':
    unittest.main()