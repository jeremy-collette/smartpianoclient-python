#!/usr/bin/python

# smartpiano Python Client
# Copyright (c) Jeremy Collette 2020.
# This software is released under the MIT license.
# See the 'LICENSE' file for more information.

import sys
from smartpianofactory import SmartPianoFactory

if __name__ != "__main__":
    sys.exit(0)

print("smartpiano Python Client v0.1.1")
print("----------------------------------------")
print("Copyright (c) 2020 Jeremy Collette.\n")

if len(sys.argv) <= 1:
    print("python3 main.py <midi_file_name> [--serial <serial_device>] [--baud <baud_rate>]")
    sys.exit(1)

midi_file_name = sys.argv[1]
serial_device = "/dev/ttyACM0"
baud_rate = "115200"

i = 2
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "--serial":
        if i == len(sys.argv)-1:
            print("Expected string after \"--serial\" option. Run without arguments to see valid options.")
            sys.exit(1)
        serial_device = sys.argv[i+1]
        i += 1  # Skip parsing option value
    elif arg == "--baud":
        if i == len(sys.argv)-1:
            print("Expected integer after \"--baud\" option. Run without arguments to see valid options.")
            sys.exit(1)
        baud_rate = sys.argv[i + 1]
        i += 1  # Skip parsing option value
    else:
        print("Unrecognised option \"" + arg + "\". Run without arguments to see valid options.")
        sys.exit(1)
    i += 1

print("midi_file_name = " + midi_file_name)
print("serial_device = " + serial_device)
print("baud_rate = " + baud_rate)

smart_piano_factory = SmartPianoFactory(serial_device, baud_rate)
smart_piano = smart_piano_factory.create_smart_piano_client(midi_file_name)
smart_piano.play_song()
