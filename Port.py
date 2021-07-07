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
        pkg = pkg.replace('\r', '')
        pkg = pkg.replace('\n', '')
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
        while True:
            try:
                recieved = self.read()
                print(f"re:{recieved}")
                if recieved != "":
                    Data = recieved.split(",")
                    print(Data)
                    if Data[0] == "R":
                        telemetry = {"TYP": str(Data[0]), "PKG": int(Data[1]), "ALT": float(Data[2]),
                                     "LAT": float(Data[3]), "LNG": float(Data[4]), "TEM": float([5]),
                                     "BAT": float(Data[6]), "ACX": float(Data[7]), "ACY": float(Data[8]),
                                     "ACZ": float(Data[9]), "GYX": float(Data[10]), "GYY": float(Data[11]),
                                     "GYZ": float(Data[12])}
                    elif Data[0] == "C":
                        telemetry = {"TYP": str(Data[0]), "PKG": int(Data[1]), "ALT": float(Data[2]),
                                     "LAT": float(Data[3]), "LNG": float(Data[4]), "GAL": float(Data[5]),
                                     "TEM": float(Data[6]), "HUM": float(Data[7]), "PRE": float(Data[8]),
                                     "BAT": float(Data[9]), "P10": float(Data[10]), "P25": float(Data[11]),
                                     "ACX": float(Data[12]), "ACY": float(Data[13]), "ACZ": float(Data[14]),
                                     "GYX": float(Data[15]), "GYY": float(Data[16]), "GYZ": float(Data[17])}
                    elif Data[0] == "G":
                        telemetry = {"TYP": str(Data[0]), "LAT": float(Data[1]), "LNG": float(Data[2]),
                                     "ALT": float(Data[3]),"MGX": float(Data[4]), "MGY": float(Data[5]),
                                     "MGZ": float(Data[6])}
                    with open(self.path, "a") as file:
                        file.write(recieved)
                    print(telemetry)
                    return telemetry
            except:
                pass


if __name__ == "__main__":
    A = Port('COM11')
    print(A.list_port())
    print(A.path())
