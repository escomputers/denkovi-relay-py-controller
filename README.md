## Denkovi Relay Board Controller v1.5.2
---

### Notes
- 4 and 8 relay boards do not handle connection to multiple devices. Connects to first found Denkovi.
- Not thread safe. 
- Possible race conditions with device plugging.
- Uses a VCP delay of 50ms. Documentation specifies 5ms but was still seeing corruption at 20ms. Could be improved for the gets by doing an initial sync and then keeping track of the states in the class.

---
### Install
```shell
python setup.py install

# Then take a look at example.py for usage instructions
```

Change Log
__________
 * 1.5.2 - Fix FT_handle type to match FTD2XX DLL library.
 * 1.5.1 - Correctly shuts down FTDI on Linux.
 * 1.5.0 - Adds ability to select from multiple FTDI devices.
 * 1.4.0 - Adds Python 3 support.
 * 1.3.2 - Uses case insensitive for the serial number comparison.
 * 1.3.1 - Fixes premature return when trying to discover first device.
 * 1.3 - setup.py package installer added.
 * 1.2 - Linux support added.
 * 1.1 - Fixed serial not being flagged as close on disconnect and failure to ensure disconnection on a reconnect.
