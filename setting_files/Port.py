try:
    from _global import *
except:
    from ._global import *
import string


class Port:
    def __init__(self, com, end: str, start=None, baudrate=9600, file_name='', key=None):
        self.com = com
        self.baudrate = baudrate
        self.end = end
        self.key = key
        self.start = start
        self.device = None
        self.path = self.path(file_name)

    @staticmethod
    def list_port():
        com = []
        for i in range(256):
            comtest = 'COM' + str(i)
            try:
                serial.Serial(comtest)
            except:
                pass
            else:
                com.append(comtest)
        return com

    def write(self, text: str):
        if self.device is not None:
            self.device.write(text.encode('utf-8'))
        else:
            print(f"Cannot write to {self.device}")

    def connect(self):
        try:
            self.device = serial.Serial(
                self.device, baudrate=self.baudrate, timeout=60)
        except:
            print(f"Cannot connect to {self.device}")

    def read(self):
        inp = self.device.read().decode('utf-8')
        pkg = ''
        while inp != self.end:
            inp = self.device.read().decode('utf-8')
            print(inp, end='')
            if self.start is not None and inp == self.start:
                pkg = ''
            if inp in string.printable:
                print(f'READ:{inp}')
                pkg += inp
        pkg = pkg.replace('\r', '').replace('\n', '')
        return pkg

    @staticmethod
    def path(file_name):
        if not os.path.exists('Data_log'):
            os.mkdir('Data_log')
        clock = datetime.now().time()
        index = "_".join(list((date.today().strftime("%b-%d-%Y"),
                         str(clock.hour).zfill(2), str(clock.minute).zfill(2))))
        return os.path.join(os.path.abspath(os.getcwd()),
                            'Data_log', f"{file_name}_{index}.csv")

    def reading(self):
        if self.device is None:
            print("No Serial device found! Try .connect to start device")
            return
        if self.key is not None:
            self.reading_key()
        else:
            self.reading_split()

    def reading_split(self):
        recieved = self.read().split(",")
        if len(recieved) != 0:
            with open(self.path, "at") as file:
                file.write(','.join(recieved))
            return recieved

    def reading_key(self):
        recieved = self.read().split(",")  # recieved from read
        with open(self.path, "at") as file:  # save file
            file.write(','.join(recieved))
        tolist = self.key[recieved[2]]  # map tolist to dict keys set
        if len(tolist) == len(recieved):  # check length
            dic = {tolist[i]: recieved[i] for i in range(len(tolist))}
            return dic
        else:
            raise AttributeError


if __name__ == "__main__":
    Allport = Port.list_port()
    for index, port in enumerate(Allport):
        print(f'{index+1}:{port}')
    com = int(input("Choose port :"))-1
    print(Allport[com])
    device = serial.Serial(Allport[com], baudrate=9600, timeout=60)
    COM = Port(device, '$')
    print(f'saving file to {COM.path}')
    while True:
        COM.rading()
