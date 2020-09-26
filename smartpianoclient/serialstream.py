# smartpiano Python Client
# Copyright (c) Jeremy Collette 2020.
# This software is released under the MIT license.
# See the 'LICENSE' file for more information.

class SerialStream:
    def __init__(self, serial, printer):
        self.serial = serial
        self.printer = printer

    def send_packet(self, data):
        self.printer.printmsg("Sending packet...")
        packet = bytearray()
        for d in data:
            packet.append(d)
        self.serial.write(packet)
        self.printer.printmsg("Sent!")

    def read_line(self):
        line = self.serial.readline().strip()
        return line

    def available_bytes(self):
        return self.serial.in_waiting
