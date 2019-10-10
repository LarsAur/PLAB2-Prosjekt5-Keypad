# from keypad import Keypad
# from led_board import LED
# from finite_state_machine import FSM


class KPC:

    def __init__(self):
        # self.keypad = Keypad()
        # self.led_board = LED()
        # self.fsm = FSM()
        self.passcode_buffer = []
        self.filename = "password.txt"
        self.override_signal = None
        self.led_id = None
        self.led_duration = None
        self.password = self.get_password(self.filename)

    def get_password(self, filename):
        """Gets password from file. If no password is saved
        in the file, it makes a standard password set to '1234'"""
        with open(filename) as f:
            password = f.read()
            password = password.strip()  # removes leading whitespace
            if not password:
                password = '1234'
            return password

    def save_password(self, filename, password):
        """Updates and saves the password to file"""
        with open(filename, "w") as f:
            f.write(password)

    def init_passcode_entry(self):
        """Clear the passcode-buffer and initiate a ”power up”
        lighting sequence on the LED Board. This should be done
        when the user first presses the keypad."""
        self.reset_passcode_buffer()
        self.led_board.leds_powering_up

    def get_next_signal(self):
        """Return the override-signal, if it is non-blank;
        otherwise query the keypad for the next pressed key."""
        if self.override_signal:
            return self.override_signal
        else:
            return self.keypad.get_next_signal()

    def verify_login(self):
        """Check that the password just entered via the keypad
        matches that in the password file. Store the result (Y or N)
        in the override-signal. Also, this should call the
        LED Board to initiate the appropriate lighting pattern for login success or failure."""
        password = ''.join(self.passcode_buffer)
        self.passcode_buffer = []
        if password == self.password:
            self.led_board.twinkle_all_leds(3)
            self.fsm.set_new_state("S-Active")
            return True
        else:
            self.led_board.flash_all_leds(3)
            self.fsm.set_new_state("S-Init")
            self.reset_agent()
            return False

    def validate_passcode_change(self):
        """Check that the new password is legal. If so, write the
        new password in the password file. Should be at least 4 digits
        long and only contain digits 0-9. Uses the LED Board to signal
        success or failure in changing the password"""
        if len(self.passcode_buffer) < 4:
            self.led_board.flash_all_leds(3)
            self.reset_passcode_buffer()
            return False
        for letter in self.passcode_buffer:
            if not letter.isdigit():
                self.led_board.flash_all_leds(3)
                self.reset_passcode_buffer()
                return False
        self.password = ''.join(self.passcode_buffer)
        self.save_password(self.filename, self.password)
        self.reset_passcode_buffer()
        self.led_board.twinkle_all_leds(3)
        return True

    def reset_agent(self):
        """initializes fields as defined in init"""
        self.reset_passcode_buffer()
        self.override_signal = None
        self.led_id = ""
        self.led_duration = ""
        self.password = self.get_password(self.filename)

    def set_led_duration(self, led_duration):
        """sets led_id"""
        self.led_duration = led_duration

    def set_led_id(self, led_id):
        """sets let_duration"""
        self.led_id = led_id

    def fully_activate_agent(self):
        pass

    def append_next_password_digit(self, digit):
        """adds (hopefully) a digit to the passcode buffer"""
        self.passcode_buffer.append(digit)

    def reset_passcode_buffer(self):
        """resets passcode_buffer"""
        self.passcode_buffer = []

    def light_one_led(self):
        """Using values stored in the Lid and Ldur slots, call the
        LED Board and request that LED Lid be turned on for Ldur seconds."""
        self.led_board.light_led(self.led_id, self.led_duration)

    def flash_leds(self):
        """Call the LED Board and request the flashing of all LEDs."""
        self.led_board.flash_all_leds()

    def twinkle_leds(self):
        """Call the LED Board and request the twinkling of all LEDs."""
        self.led_board.twinkle_all_leds()

    def exit_action(self):
        """Call the LED Board to initiate the ”power down” lighting sequence."""
        self.led_board.leds_powering_down()


if __name__ == "__main__":
    kpc = KPC()
