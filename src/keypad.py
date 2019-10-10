import time
import RPi.GPIO as GPIO

class Keypad:

    

    def __init__(self):
        """Initializes all pins and a pins_to_key dictionary"""
        self.col_pins = [17, 27, 22]
        self.row_pins = [18, 23, 24, 25]
        # Indexed with (column_pin, row_pin)
        self.pin_to_key = {(17, 18):1, (17, 23):4, (17, 24):7, (17, 25):"*",
                           (27, 18):2, (27, 23):5, (27, 24):8, (27, 25):0,
                           (22, 18):3, (22, 23):6, (22, 24):9, (22, 25):"#" }

        self.poll_repeat_checks = 20
        self.poll_delay = 0.010 #10ms

    def setup(self):
        """Setting up GPIO pins for the keypad"""
        GPIO.setmode(GPIO.BCM)
        # Setting up column pins to input mode and pull_down
        for pin in self.col_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Setting up row pins to output mode
        for pin in self.row_pins:
            GPIO.setup(pin, GPIO.OUT)

    def do_polling(self):
        """Polls the keypad buttons for buttonpresses, returns the pin values of the button"""
        for rpin in self.row_pins:
            GPIO.output(rpin, GPIO.HIGH)
            for cpin in self.col_pins:
                repeat = 0
                # checks the pin 20 times with a delay of 10ms
                for i in range(self.poll_repeat_checks):
                    time.sleep(self.poll_delay)
                    if GPIO.input(cpin) == GPIO.LOW:
                        break
                    else:
                        repeat += 1
                
                if repeat == self.poll_repeat_checks:
                    return (cpin, rpin)
                    
            GPIO.output(rpin, GPIO.LOW)

        return None

    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected."""
        polled_pins = None
        while not polled_pins:
            polled_pins = self.do_polling()
        
        return self.pin_to_key(polled_pins)
            

