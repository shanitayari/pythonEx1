import pytest
from Car.car import Car
from Car.log import Log
from dotenv import load_dotenv
import os
@pytest.fixture
def car():
    load_dotenv()
    return Car()
def test_gearUp(car):
    """test gear up"""
    try:
        car.start()
        car.gearUp()
        assert car.gear==1
        Log().printToFile("test_gearUp passed")
    except AssertionError as assertionError:
        Log().printToFile("test_gearUp failed "+str(assertionError))
def test_gearUpInStop(car):
    """test gear up in stop"""
    try:
        with pytest.raises(Exception):
            car.gearUp()
        Log().printToFile("test_gearUpInStop passed")
    except AssertionError as assertionError:
        Log().printToFile("test_gearUpInStop failed "+str(assertionError))
def test_gearDown(car):
    """test gear down"""
    try:
        car.start()
        car.gearUp()
        car.gearDown()
        assert car.gear==0
        Log().printToFile("test_gearDown passed")
    except AssertionError as assertionError:
        Log().printToFile("test_gearDown failed "+str(assertionError))
def test_gearDownLessMin(car):
    """test gear down less than min"""
    try:
        with pytest.raises(Exception):
            car.gearDown()
        Log().printToFile("test_gearDownLessMin passed")
    except AssertionError as assertionError:
        Log().printToFile("test_gearDownLessMin failed "+str(assertionError))
def test_start(car):
    """test start the car"""
    try:
        car.start()
        assert car.isStart==True
        Log().printToFile("test_start passed")
    except AssertionError as assertionError:
        Log().printToFile("test_start failed "+str(assertionError))
def test_startInDrive(car):
    """test start in drive"""
    try:
        car.start()
        car.gearUp()
        with pytest.raises(Exception):
            car.start()
        Log().printToFile("test_startInDrive passed")
    except AssertionError as assertionError:
        Log().printToFile("test_startInDrive failed "+str(assertionError))
def test_stop(car):
    """test stop the car"""
    try:
        car.stop()
        assert car.isStart==False
        assert car.isDrive==False
        assert car.gear==0
        Log().printToFile("test_stop passed")
    except AssertionError as assertionError:
        Log().printToFile("test_stop failed "+str(assertionError))
def test_drive(car):
    """test drive x km"""
    try:
        car.start()
        car.drive(5)
        assert car.fuel==int(os.getenv("fuelInit"))-5/car.fuelConsumption
        Log().printToFile("test_drive passed")
    except AssertionError as assertionError:
        Log().printToFile("test_drive failed "+str(assertionError))
def test_driveInStop(car):
    """test drive in stop"""
    try:
        with pytest.raises(Exception):
            car.drive(5)
        Log().printToFile("test_driveInStop passed")
    except AssertionError as assertionError:
        Log().printToFile("test_driveInStop failed "+str(assertionError))