from dotenv import load_dotenv
import os
import datetime
class Log:
    def __init__(self):
        """create new log handler"""
        load_dotenv()
    def printToFile(self,message):
        """print log to log file"""
        file=open(os.getenv("filePath"),"a")
        file.write(str(datetime.datetime.now())+" "+message+"\n")
        file.flush()
        file.close()