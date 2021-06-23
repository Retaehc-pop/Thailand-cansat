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
            print("[Cannot connect port]", end="")

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

    def reading(self):
        try:
            recieved = self.read()
            if recieved != "":
                Data = recieved.split(",")
                with open(self.path, "a") as file:
                    file.write(recieved)
                return Data
        except:
            pass


if __name__ == "__main__":
    A = Port('COM11')
    print(A.list_port())
    print(A.path())
