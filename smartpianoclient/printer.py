# smartpiano Python Client
# Copyright (c) Jeremy Collette 2020.
# This software is released under the MIT license.
# See the 'LICENSE' file for more information.

from datetime import datetime


class Printer:
    def printmsg(self, msg):
        print("[" + str(datetime.now().time()) + "] " + msg)
