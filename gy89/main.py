from lsm303d import LSM303D
import time
lsm = LSM303D(0x1e)
lsm.setup()
while True:
    accel_x, accel_y, accel_z = lsm.accelerometer()
    print(f"İvmeölçer: X={accel_x}, Y={accel_y}, Z={accel_z}")
    time.sleep(0.5)



