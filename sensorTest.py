import time
import pi2go2

pi2go2.init(0)

try:
    while True:
        dist = pi2go2.getDistance()
        print("Distance: ", int(dist))
        irLeftLine = pi2go2.irLeftLine()
        irRightLine = pi2go2.irRightLine()
        print("Left line: {}\nRight line: {}".format(irLeftLine, irRightLine))
        irLeft = pi2go2.irLeft()
        irRight = pi2go2.irRight()
        print("Left: {}\nRight: {}".format(irLeft, irRight))
        irCenter = pi2go2.irCenter()
        print("Center: {}".format(irCenter))
        irAny = pi2go2.irAll()
        print("Any: {}".format(irAny))
        battery = pi2go2.getBatteryMonitor()
        print("Battery monitor: {}".format(battery))
        switch = pi2go2.getSwitch()
        print("Button switch: {}".format(switch))
        print()
        time.sleep(1)

except KeyboardInterrupt:
    print()
    pass

finally:
    pi2go2.cleanup()
