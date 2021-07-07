import serial
import os
import time
from datetime import datetime, date


class Port:
    def __init__(self, device):
        self.device = device
        self.path = self.path()
        self.end = "$"

    @staticmethod
    def list_port():
        available = []
        for i in range(256):
            comtest = 'COM' + str(i)
            try:
                serial.Serial(comtest)
            except:
                pass
            else:
                available.append(comtest)
        return available

    def connect_port(self, baudrate):
        try:
            self.device = serial.Serial(self.device, baudrate=int(baudrate), timeout=60)
        except:
            print("[Cannot connect port]", end=" ")

    def read(self):
        telemetry = ""
        pkg = ''
        while telemetry != self.end:
            pkg += telemetry
            telemetry = self.device.read().decode('utf-8')
        pkg.replace('\r', '')
        pkg.replace('\n', '')
        return pkg

    def path(self):
        clock = datetime.now().time()
        today = date.today()
        timestp = str('%02d' % clock.hour) + '_' + str('%02d' % clock.minute)
        datano = str(timestp) + '_' + str(today.strftime("%b-%d-%Y"))
        return f"DATA/DATA-{datano}.csv"

    # def reading(self):
    #     try:
    #         recieved = self.read()
    #         if recieved != "":
    #             Data = recieved.split(",")
    #             with open(self.path, "a") as file:
    #                 file.write(recieved)
    #             return Data
    #     except:
    #         pass

    def reading(self):
        try:
            recieved = self.read()
            if recieved != "":
                Data = recieved.split(",")
                if Data[0] == "R":
                    telemetry = {"TYP": Data[0],"PKG": Data[1],"ALT": Data[2],
                                 "LAT": Data[3],"LNG": Data[4],"TEM": Data[5],
                                 "BAT": Data[6],"ACX": Data[7],"ACY": Data[8],
                                 "ACZ": Data[9],"GYX": Data[10],"GYY": Data[11],"GYZ": Data[12]}
                elif Data[0] == "C":
                    telemetry = {"TYP": Data[0],"PKG": Data[1],"ALT": Data[2],
                                 "LAT": Data[3],"LNG": Data[4],"GAL": Data[5],
                                 "TEM": Data[6],"HUM": Data[7],"PRE": Data[8],
                                 "BAT": Data[9],"P10": Data[10],"P25": Data[11],
                                 "ACX": Data[12],"ACY": Data[13],"ACZ": Data[14],
                                 "GYX": Data[15],"GYY": Data[16],"GYZ": Data[17]}
                elif Data[0] == "G":
                    telemetry = {"TYP" : Data[0],"LAT": Data[1],"LNG": Data[2], "ALT": Data[3],
                                 "MGX": Data[4],"MGY": Data[5],"MGZ": Data[6]}
                with open(self.path, "a") as file:
                    file.write(recieved)
                return telemetry
        except:
            pass


if __name__ == "__main__":
    A = Port('COM11')
    print(A.list_port())
    print(A.path())
