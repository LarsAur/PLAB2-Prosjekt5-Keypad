import time
import RPi.GPIO as GPIO

class Keypad:

    def __init__(self):
        """Initializes all pins and a pins_to_key dictionary"""
        self.col_pins = [17, 27, 22]
        self.row_pins = [18, 23, 24, 25]
        # Indexed with (column_pin, row_pin)
        self.pins_to_key = {(17, 18): '1', (17, 23): '4', (17, 24): '7', (17, 25): '*',
                            (27, 18): '2', (27, 23): '5', (27, 24): '8', (27, 25): '0',
                            (22, 18): '3', (22, 23): '6', (22, 24): '9', (22, 25): '#'}

        self.poll_repeat_checks = 20
        self.poll_delay = 0.010  # 10ms

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
        repeats = [[0 for i in range(len(self.row_pins))] for j in range(len(self.col_pins))]
        # checks the pin 20 times with a delay of 10ms  
        for i in range(self.poll_repeat_checks):
            for rpin in range(len(self.row_pins)):
                GPIO.output(self.row_pins[rpin], GPIO.HIGH)
                for cpin in range(len(self.col_pins)):                   
                    if GPIO.input(self.col_pins[cpin]) == GPIO.HIGH:
                        repeats[cpin][rpin] += 1
                    if repeats[cpin][rpin] == self.poll_repeat_checks:
                        return (self.col_pins[cpin], self.row_pins[rpin])

                GPIO.output(self.row_pins[rpin], GPIO.LOW)
                time.sleep(self.poll_delay)
        return None


    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should
        initiate repeated calls to do polling until a key press is detected."""
        polled_pins = None
        while not polled_pins:
            polled_pins = self.do_polling()

        return self.pins_to_key[polled_pins]


if __name__ == "__main__":

    kp = Keypad()
    kp.setup()
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26, GPIO.LOW)

    if(kp.get_next_signal() == 0):
        GPIO.output(26, GPIO.HIGH)

    time.sleep(1)

    if(kp.get_next_signal() == "#"):
        GPIO.output(26, GPIO.LOW)
