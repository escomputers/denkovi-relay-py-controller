"""Wrapper around the pylibftdi library"""

from __future__ import print_function

import re

from pylibftdi import BitBangDevice, Driver

from . import dae_RelayBoard_Common


class FTD2XXLinux(object):
    def __init__(self):
        self.driver = Driver()
        self.bb = None
        self.comport = None

    def initialise(self, deviceID, baudRate, mask, bitMode):
        try:
            indexed = deviceID.split("#", 2)

            if len(indexed) == 2:
                deviceID = indexed[0]
                which = int(indexed[1])
            else:
                which = 0

            index = 0
            found = False
            for dev in self.driver.list_devices():
                if re.search(deviceID + ".+", dev[2]):
                    if which == index:
                        found = True
                        print("Found device %s#%d => %s" % (deviceID, index, dev[2]))
                        deviceID = dev[2]
                        break
                    index += 1

            if found:
                self.bb = BitBangDevice(deviceID)
                self.bb.direction = mask
                self.bb.open()
        except Exception as e:
            raise dae_RelayBoard_Common.Denkovi_Exception(
                "Could not connect to relay board: %s: %s" % (e.__class__, e)
            )
        if not found:
            raise dae_RelayBoard_Common.Denkovi_Exception(
                "Relay board: %s#%d not found" % (deviceID, index)
            )

    def close(self):
        if self.bb is not None:
            self.bb.close()
            self.bb = None

    def writeByte(self, byte):
        if self.bb is None:
            raise dae_RelayBoard_Common.Denkovi_Exception("Board non initialized")
        self.bb.port = byte

    def readByte(self):
        if self.bb is None:
            raise dae_RelayBoard_Common.Denkovi_Exception("Board non initialized")
        return self.bb.port
