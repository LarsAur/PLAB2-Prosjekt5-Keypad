"""The class handling the LED board"""

import time
import RPi.GPIO as GPIO


class LED:
    """The lED class"""

    def __init__(self):
        self.pin0 = 6
        self.pin1 = 13
        self.pin2 = 19
        self.single_led_handling = {0: (self.pin2, self.pin0, self.pin1, self.pin0, self.pin1),
                                    1: (self.pin2, self.pin0, self.pin1, self.pin1, self.pin0),
                                    2: (self.pin0, self.pin1, self.pin2, self.pin1, self.pin2),
                                    3: (self.pin0, self.pin1, self.pin2, self.pin2, self.pin1),
                                    4: (self.pin1, self.pin0, self.pin2, self.pin0, self.pin2),
                                    5: (self.pin1, self.pin0, self.pin2, self.pin2, self.pin0)
                                    }

    def setup(self):
        """Set the proper mode via: GPIO.setmode(GPIO.BCM)."""
        GPIO.setmode(GPIO.BCM)

    def light_led(self, led_id):
        """Turn on one of the 6 LEDs by making the appropriate
        combination of input and output declarations, and then
        making the appropriate HIGH / LOW settings on #the output pins."""
        led_order = self.single_led_handling[led_id]
        GPIO.setup(led_order[0], GPIO.IN)
        GPIO.setup(led_order[1], GPIO.OUT)
        GPIO.setup(led_order[2], GPIO.OUT)
        GPIO.output(led_order[3], GPIO.HIGH)
        GPIO.output(led_order[4], GPIO.LOW)

    def flash_one_led(self, led_id, led_duration):
        """Flash one chosen of the 6 LEDs on for k seconds,
        where k is an argument of the method."""
        timeout = led_duration  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            self.light_led(led_id)
        self.light_off_led()

    def light_off_led(self):
        """Turn off all LEDs"""
        GPIO.setup(self.pin0, GPIO.IN)
        GPIO.setup(self.pin1, GPIO.IN)
        GPIO.setup(self.pin2, GPIO.IN)

    def flash_all_leds(self, led_duration):
        """Flash all 6 LEDs on and off for k seconds,
        where k is an argument of the method."""
        timeout = led_duration  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in range(6):
                self.light_led(i)
        self.light_off_led()

    def twinkle_all_leds(self, led_duration):
        """Turn all LEDs on and off in sequence for k seconds,
        where k is an argument of the method."""
        timeout = led_duration  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            for i in range(6):
                self.light_led(i)
                time.sleep(0.01)
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
    TEST_LED = LED()
    TEST_LED.setup()
    TEST_LED.leds_powering_down()
