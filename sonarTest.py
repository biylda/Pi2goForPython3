import time
import pi2go2

pi2go2.init(0)

try:
    while True:
        dist = pi2go2.getDistance()
        print("Distance 0: ", int(dist))
        print()
        time.sleep(1)

except KeyboardInterrupt:
    print()
    pass

finally:
    pi2go2.cleanup()
