# Network-Restarter
Code for an RPi 3B to send 3.3v out of pin 21 when WiFi is lost to reset it

# Explanation
The RPi sends a ping to another webserver on the local network to check if it is online and if not assumes the network is down and restarts the ONT box via relay. Pin 21 always has 3.3v going to it holding open the relay until it fails to talk to the webserver and cuts power for 10 seconds and then turns it back on until it gets a good signal and is able to turn off power again if it wants.
