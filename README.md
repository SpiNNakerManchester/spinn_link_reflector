# spinn_link_reflector
this module contains code to use an algorithm to place routing table entries
that ensure all packets coming into spinnaker via the SpiNNlinks are sent
directly back out the same SpiNNLink. It allows verification of the FPGA code
that it can recieve and send MC packets correctly.

# To use

1. pull off from github
2. choose which front end interface method to use out of the main_calls module.
This is either:

2.1. PyNN 0.7 interface via the pynn7_reflector.py
2.2. PyNN 0.8/0.9 interface via the pynn8_reflector.py
2.3. GFE interface via the gfe_reflector.py

3. run choosen script.

worth noting that in PyNN 0.8 /0.9 we do not yet support run forever
 functionality. So it runs for 2^31 milliseconds.