from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "ObsTwitchStream",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x008080, "MPS", [Keycode.F13]),
        (0x008000, "MS", [Keycode.F14]),
        (0x101010, "BD", [Keycode.F15]),
        # 2nd row ----------
        (0x101010, "BK", [Keycode.F16]),
        (0x101010, "BDK", [Keycode.F17]),
        (0x101010, "BP", [Keycode.F18]),
        # 3rd row ----------
        (0xFF0000, "Sec", [Keycode.F19]),
        (0xFF0000, "Mute", [Keycode.F20]),
        (0xff8c00, "Brb", [Keycode.F21]),
        # 4th row ----------
        (0x008000, "Start", [Keycode.F22]),
        (0x778899, "End", [Keycode.F23]),
        (0xFF0000, "Stop", [Keycode.F24]),
    ],
}
