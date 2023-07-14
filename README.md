# Marvelmind-client-server

## Description

Marvelmind-client-server — this is an example of using marvelmind-python to pass data through client server architecture

## Borrowing

The original examples can be found at the repository link below:
* https://github.com/MarvelmindRobotics/marvelmind.py

## Running examples

Install the file echo_server.py on the computer (robot) that will send data about the position of the marvelmind beacon by changing it:
* adr - address of mobile beacon (from Dashboard) for data filtering. If it is None, every read data will be appended to buffer.
* tty - serial port device name (physical or USB/virtual). It should be provided as an argument:

```
/dev/ttyACM0 — typical for Linux
/dev/tty.usbmodem1451 — typical for Mac OS X
/COM0 — typical for Windows
```

* HOST - IP address of the device in the local network

### The server part is launched with the command:

```
python3 echo_server.py
```

### After that, run client.py on the user's PC:
```
python3 echo_server.py
```

## Result
After connecting to the server, the user's PC will display the position of the beacon and the angle of rotation relative to the 2nd beacon associated with it
```
x = 2.11, y = 4.31, angle = 92.4
x = 2.14, y = 4.33, angle = 92.4
x = 2.17, y = 4.35, angle = 92.4
x = 2.21, y = 4.37, angle = 92.4
```



