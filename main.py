from car import Car
from log import Log
if __name__=='__main__':
    try:
        log=Log()
        car=Car()
        car.toFuel()
    except Exception as exception:
        log.printToFile(str(exception))