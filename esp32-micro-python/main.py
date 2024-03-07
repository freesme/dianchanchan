import time

from lib.motor import motor_step

if __name__ == '__main__':
    motor_step(1)
    time.sleep_ms(3)
    motor_step(1, direction=-1)
