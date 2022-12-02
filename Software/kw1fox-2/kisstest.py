#!/usr/bin/env python
"""
Reads & Prints KISS frames from a TCP Socket.

For use with programs like Dire Wolf.
"""

import aprs
import kiss
import time


def main():
    # frame = aprs.Frame()
    # frame.source = aprs.Callsign("KW1FOX-2")
    # frame.destination = aprs.Callsign("KW1FOX-1")
    # frame.path = [aprs.Callsign("WIDE1-1")]
    # frame.info = ">Hello World!"

    ki = kiss.TCPKISS(host="10.85.3.154", port=8001)
    ki.start()

    for i in range(4):
        # This is messy, kiss has some regressions in replace that cause issues!
        ki.write(f"KW1FOX-2>KW1FOX-1:Hello {i}!")
        time.sleep(2)


if __name__ == "__main__":
    main()
