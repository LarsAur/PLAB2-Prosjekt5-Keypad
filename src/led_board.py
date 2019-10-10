'''The class handling the LED board'''

import RPi.GPIO as GPIO
import time


class LED:
    '''The lED class'''

    def __init__(self):
        self.PIN0 = 6
        self.PIN1 = 13
        self.PIN2 = 19
        self.single_led_handling = {0: (self.PIN2, self.PIN0, self.PIN1, self.PIN0, self.PIN1),
                                    1: (self.PIN2, self.PIN0, self.PIN1, self.PIN1, self.PIN0),
                                    2: (self.PIN0, self.PIN1, self.PIN2, self.PIN1, self.PIN2),
                                    3: (self.PIN0, self.PIN1, self.PIN2, self.PIN2, self.PIN1),
                                    4: (self.PIN1, self.PIN0, self.PIN2, self.PIN0, self.PIN2),
                                    5: (self.PIN1, self.PIN0, self.PIN2, self.PIN2, self.PIN0)
                                    }

    def setup(self):
        """Set the proper mode via: GPIO.setmode(GPIO.BCM)."""
        GPIO.setmode(GPIO.BCM)

    def light_led(self, led_id):
        """Turn on one of the 6 LEDs by making the appropriate #combination of input and output declarations,
        and #then making the appropriate HIGH / LOW settings on #the output pins."""
        led_order = self.single_led_handling[led_id]
        GPIO.setup(led_order[0], GPIO.IN)
        GPIO.setup(led_order[1], GPIO.OUT)
        GPIO.setup(led_order[2], GPIO.OUT)
        GPIO.output(led_order[3], GPIO.HIGH)
        GPIO.output(led_order[4], GPIO.LOW)

    def light_off_led(self):
        """Turn off all LEDs"""
        GPIO.setup(self.PIN0, GPIO.IN)
        GPIO.setup(self.PIN1, GPIO.IN)
        GPIO.setup(self.PIN2, GPIO.IN)

    def flash_all_leds(self, led_duration):
        """Flash all 6 LEDs on and off for k seconds, where k is #an argument of the method."""
        timeout = led_duration  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in range(6):
                self.light_led(i)
        self.light_off_led()

    def twinkle_all_leds(self, led_duration):
        """Turn all LEDs on and off in sequence for k seconds, #where k is an argument of the method."""
        timeout = led_duration  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in range(6):
                self.light_led(i)
                time.sleep(0.1)
        self.light_off_led()

    def leds_powering_up(self):
        """Flash LEDs at startup"""
        timeout = 3  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in [0, 4, 2]:
                self.light_led(i)
        self.light_off_led()

    def leds_powering_down(self):
        """"Flash LEDs at shutdown"""
        timeout = 3  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in [1, 5, 3]:
                self.light_led(i)
        self.light_off_led()


if __name__ == '__main__':
    led = LED()
    led.setup()
    led.leds_powering_down()
