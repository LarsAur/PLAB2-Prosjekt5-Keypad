class LED:

    def __init__(self):
        pass

    def setup(self):
        """Set the proper mode via: GPIO.setmode(GPIO.BCM)."""
        pass

    def light_led(self, led_id, led_duration):
        """Turn on one of the 6 LEDs by making the appropriate #combination of input and output declarations, and #then making the appropriate HIGH / LOW settings on #the output pins."""
        pass

    def flash_all_leds(self, led_duration):
        """Flash all 6 LEDs on and off for k seconds, where k is #an argument of the method."""
        pass

    def twinkle_all_leds(self, led_duration):
        """Turn all LEDs on and off in sequence for k seconds, #where k is an argument of the method."""
        pass

    def leds_powering_up(self):
        """Flash LEDs at startup"""
        pass

    def leds_powering_down(self):
        """"Flash LEDs at shutdown"""
        pass
