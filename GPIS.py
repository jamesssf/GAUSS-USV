## Nick Purcell - 2019
# GAUSS-R ASV Team
# Python Library for Titan X1 GPS
# Based on Arduino code for GPS module
# https://github.com/sparkfun/SparkFun_I2C_GPS_Arduino_Library/blob/master/src/SparkFun_I2C_GPS_Arduino$# https://github.com/sparkfun/SparkFun_I2C_GPS_Arduino_Library/blob/master/src/SparkFun_I2C_GPS_Arduino$
from smbus2 import SMBus
import operator
from time import sleep


# Address of MT33x (0x10)
MT333x_ADDR = 0x10

# This is a limitation of the counter variable "head"
# in the arduino code being an 8-bit unsigned int, might
# not be an issue with the pi
MAX_PACKET_SIZE = 255

# I2C speed
I2C_SPEED_STANDARD = 100000
I2C_SPEED_FAST = 400000

# I2C channel, will always be 1 for GPIO
channel = 1

# I2C Bus variable
bus = SMBus(channel)

class I2CGPS:

    # Location of the next available spot in the gpsData array, limited to 255
    _head = 0
    # Location of last spot read from gpsData array, limited to 255
    _tail = 0

    # Flag to print the serial commands we are sending to the serial port for debug
    _printDebug = False

    # Empty list for gps data
    gpsData = [0] * MAX_PACKET_SIZE

    # Set up I2C
    def begin(self):
        # Initialize I2C
        bus = SMBus(channel)

        # Reset _head and _tails
        self._tail = 0

    def check(self):
        # Read new data from GPS and check if different from old data
        # If data is new append it to gpsData array
        for x in range (0, 255):
            # Pull in a byte from the GPS and check if it's new.
            incoming = bus.read_byte_data(MT333x_ADDR, 1)
            if incoming != 0x0A:
                # Record the byte
                self.gpsData[self._head] = incoming
                self._head += 1
                self._head %= MAX_PACKET_SIZE
                if self._printDebug and self._head == self._tail:
                   print("Buffer Overrun")

    # Return num of available bytes that can be read
    def available(self):
        # If tail = head then there is no new available data in the buffer
        # Check to see if the module has anything in the buffer
        if self._tail == self._head:
            self.check()

        # Return new data count
        if self._head > self._tail:
            return self._head - self._tail
        if self._tail > self._head:
            return MAX_PACKET_SIZE - self._tail + self._head
        # No data available
        return 0

        # Return the next available byte from the gps data array
        # Return 0 if no byte available

    def read(self):
        if self._tail != self._head:
            datum = self.gpsData[self._tail]
            self._tail += 1
            self._tail %= MAX_PACKET_SIZE
            return datum
        return 0

    def enableDebugging(self):
        self._printDebug = True

    def disableDebugging(self):
        self._printDebug = False

    # Send commands to the GPS module

    # Send a give command or config string to the module
    # THe input buffer on the MTK is 255 bytes.  Strings
    # Must be that short.  Delay 10ms after transmission
    def sendMTKpacket(self, command):
        if len(command) > 255:
            if self._printDebug:
                print("Message too long!")
            return False
        # Transmit 7 chunks of 32 Bytes
        for chunk in range(0, 15):
            if chunk*16 >= len(command):
                break
            comChunk = [ord(command[chunk * 16])]
            for x in range(1, 16):
                if len(command) <= chunk * 16 + x: # Done sending bytes
                    break
                comChunk.append(ord(command[chunk * 16 + x]))
            bus.write_i2c_block_data(MT333x_ADDR, 0, comChunk)
            sleep(.01);     # Process bytes for 10mS
        return True

    # Given a packetType and settings return string that is a full
    # config sentence with CRC and \r \n ending bytes
    # PMTK uses different packet numbers to configure the module
    # These vary from 0 to 999.
    # https://www.sparkfun.com/datasheets/GPS/Modules/PMTK_Protocol.pdf
    def createMTKpacket(self, packetType, datafield):
        configSentence = ""
        configSentence += "PMTK"
        dataField = datafield.encode("utf-8")
        if packetType < 100:
            configSentence += "0"
        if packetType < 10:
            configSentence += "0"
        configSentence += str(packetType)

        if len(dataField) > 0:
            configSentence += dataField

        configSentence += "*" +  str(self.calcCRCforMTK(configSentence))

        configSentence = "$" + configSentence

        configSentence += "\r"
        configSentence += "\n"

        return configSentence

    def calcCRCforMTK(self, sentence):
        calc_cksum = reduce(operator.xor, (ord(s) for s in sentence), 0)
        return ("0x%X" % calc_cksum).rstrip("L").lstrip("0x") or "0"


