import serial


class TeamsSerial:
    def __init__(self,usbdevice,baudrate):
        self.usbdevice = usbdevice
        self.baudrate = baudrate

        self.ser = serial.Serial(self.usbdevice,self.baudrate,timeout=1)
    
    def senddata(self,data):
        self.ser.write(bytes(data,'utf-8'))

    def readdata(self):
        data =[]
        new_char = "\0"

        while new_char != '\r':
            new_char = self.ser.read()
            data.append(new_char)
        
        return data


if __name__ == '__main__':
    s = TeamsSerial("/dev/ttyACM0", 115200)

    from time import sleep

    while True:
        s.senddata("oof\n\r")
        sleep(1)
        s.senddata("online\r\n")
        sleep(1)