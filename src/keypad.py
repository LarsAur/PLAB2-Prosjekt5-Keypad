import time
import RPi.GPIO as GPIO

class Keypad:

    def __init__(self):
        """Setting up GPIO pins for the keypad"""
        GPIO.setmode(GPIO.BCM)
        self.col_pins = [17, 27, 22]
        self.row_pins = [18, 23, 24, 25]
        self.repeat_poll_keys = (
        [[0 for i in range(len(self.col_pins))] for j in range(len(self.row_pins))])
        
        for pin in self.col_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        for pin in self.row_pins:
            GPIO.setup(pin, GPIO.OUT)

    def poll_buttons(self):
        for rpin in range(len(self.row_pins)):
            GPIO.output(self.row_pins[rpin], GPIO.HIGH)
            for cpin in range(len(self.col_pins)):
              if GPIO.input(self.col_pins[cpin]) == GPIO.HIGH:
                self.repeat_poll_keys[cpin][rpin] += 1
              else:
                self.repeat_poll_keys[cpin][rpin] = 0
            GPIO.output(rpin, GPIO.LOW)

    def get_buttons_down(self):
        return [[self.repeat_poll_keys[i][j] == 10 for i in range(len(self.col_pins))] for j in range(len(self.row_pins))]

if __name__ == "__main__":
  kp = Keypad()
  print(kp.get_buttons_down)
