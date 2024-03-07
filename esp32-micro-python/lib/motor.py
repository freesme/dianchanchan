from machine import Pin
import time

a = Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(16, Pin.OUT)


def motor_step(circle, delay=3, direction=1):
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    pins = [a, b, c, d]
    if direction == -1:
        pins = [d, c, b, a]
    for z in range(520 * circle):
        for i in range(len(pins)):
            # Set only one pin to high at a time
            for pin_index, pin in enumerate(pins):
                pin.value(1 if pin_index == i else 0)

            # Wait for the specified delay
            time.sleep_ms(delay)
