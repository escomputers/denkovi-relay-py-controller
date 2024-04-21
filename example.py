"""Example code"""
import time
import dae_RelayBoard

dr = dae_RelayBoard.DAE_RelayBoard(dae_RelayBoard.DAE_RELAYBOARD_TYPE_8)

# You can manually set COM port like this
# COMPORT = "COM8"
# dr.initialise(COMPORT)


dr.initialise()
# dr.setState(8,False)
# time.sleep(0.5)
# print(dr.getState(8))
# print(dr.getStates())
dr.disconnect()

# List devices
# for dev in pylibftdi.Driver().list_devices():
#     print(dev)
