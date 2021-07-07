import serial


def reading(device):
    while True:
        i = device.read().decode('utf-8')
        print(i, end="")


def select_port():
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


if __name__ == "__main__":
    p = select_port()
    print(p)
    c = int(input("select port number(0-n):"))
    device = serial.Serial(port=p[c], baudrate=9600)
    reading(device)
