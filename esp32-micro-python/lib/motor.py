from machine import Pin
import time

a = Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(16, Pin.OUT)


# Control the stepper motor
def motor_step(circles, delay=3, direction=1):
    pins = [a, b, c, d]
    steps_per_revolution = 4  # 4 steps per lap
    step_sequence = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1)
    ]

    if direction == -1:
        step_sequence.reverse()

    total_steps = steps_per_revolution * 520 * circles

    for step in range(total_steps):
        for pin, state in zip(pins, step_sequence[step % steps_per_revolution]):
            pin.value(state)
        time.sleep_ms(delay)
