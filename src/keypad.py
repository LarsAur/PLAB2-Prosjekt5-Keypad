import RPi.GPIO as GPIO

class keypad:

    def __init__(self):
        """Setting up GPIO pins for the keypad"""
        GPIO.setmode(GPIO.BCM)
        self.col_pins = [17, 27, 22]
        self.row_pins = [18, 23, 24, 25]
        
        for pin in col_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        for pin in row_pins:
            GPIO.setup(pin, GPIO.OUT)

    
