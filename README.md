# smartpianoclient-python

**NOTE: Please note this project is still in alpha phase. Some features may be incomplete and/or may not meet quality standards. Show your support by reporting and/or fixing bugs.**

**NOTE: This repository contains the smartpiano Python _client_ codebase. If you're looking for the smartpiano Arduino server codebase, please see the [smartpiano](https://github.com/jeremy-collette/smartpiano) repository.**

smartpiano is a free & open-source project that lights up keys on a piano or digital keyboard to play a selected MIDI song. This is achieved using a PC running a smartpiano client, an Arduino running the smartpiano server, and a strip of LEDs which are placed on the instrument. This repository contains the source code for the Python smartpiano client.

## License
The smartpiano Python client is released as free software under the MIT license. Please note that there may be some conditions that apply to the free use and distribution of this software. Please see the LICENSE file for more information.

## Disclaimer of Warranty
Please note that this project is provided "as is", without warranty of any kind, either expressed or implied. If you choose to use the source code or software provided as part of this project, or choose to follow the instructions provided (here or anywhere else in the project) to assemble a smartpiano server (or any other device), please note that you are doing this at your own risk. Any instructions provided may be inaccurate or incomplete, or may be inapplicable to your situtation.

## Requirements
### Hardware
  * An Arduino hosting a [smartpiano server](https://github.com/jeremy-collette/smartpiano).

### Software
  * Python3 (with pip installed) to run the smartpiano Python client code
    - PyCharm is recommended for editing the smartpiano Python client code
  * A MIDI file to play

## Running the client
**NOTE: If you have a "Serial Monitor" connected to the Arduino smartpiano server, make sure you close it before you try to run the smartpiano client. Otherwise the client will not be able to connect to the Arduino using the serial port.**

Once you have an Arduino running the smartpiano server code, you can connect to it using the smartpiano Python client to play a song:
1. Navigate to the "smartpianoclient" folder in your favorite terminal.
2. Install the required dependencies:
```sh
pip3 install pyserial==3.4
pip3 install mido==1.2.9
```
3. Run the client with no arguments to see available options:
```sh
python3 main.py
```
4. Run the client with a specified MIDI file. For example:
```sh
python3 main.py "~/Desktop/some_midi_file.mid"
```

## Play at Carnegie Hall
Now that you're all setup and playing piano. It's time to practice, practice, practice!
