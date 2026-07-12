# macropad-rp2040-macros

CircuitPython configuration and macro definitions for my [Adafruit MACROPAD
RP2040](https://www.adafruit.com/product/5100), used mainly for stream
control (OBS/Twitch) while streaming public cloud (AWS, GCP) content, DIY
projects, and occasional games (mostly ATC-related).

## Repository contents

| File / folder                  | Purpose                                                            |
|---------------------------------|---------------------------------------------------------------------|
| `code.py`                       | Main macro/hotkey runtime that runs on the board                    |
| `keyconfig.py`                  | Shared key label and LED color constants                            |
| `macros/`                       | Per-application macro sets (one `.py` file per app, loaded by `code.py`) |
| `BOARD_INFO.txt`                | Firmware/board info captured from the device's `boot_out.txt`       |
| `DEVICE_LIBRARIES.txt`          | Manifest of third-party CircuitPython libraries required in `/lib` on the device |

## Hardware

- Board: Adafruit MACROPAD RP2040
- Firmware: CircuitPython (version recorded in `BOARD_INFO.txt`)

## Installing CircuitPython on the board

1. Download the CircuitPython UF2 firmware for the MACROPAD RP2040 from the
   [CircuitPython downloads page](https://circuitpython.org/board/adafruit_macropad_rp2040/).
   Use the same version recorded in `BOARD_INFO.txt` for consistency, or a
   newer stable release.
2. Put the board into bootloader mode:
   - Unplug the MACROPAD, then hold down the key labeled **BOOT** (the small
     button on the back) while plugging the USB-C cable back in, or
   - If CircuitPython is already running, double-press the **RESET** button
     on the back of the board.
3. The board will mount as a USB drive named `MACROPADBOOT`.
4. Copy the downloaded `.uf2` file onto the `MACROPADBOOT` drive.
5. The board will automatically reboot and re-mount as a drive named
   `CIRCUITPY` — CircuitPython is now installed.

## Installing the required libraries

The scripts depend on a handful of Adafruit CircuitPython bundle libraries
that are not committed to this repo (they are third-party binaries). See
`DEVICE_LIBRARIES.txt` for the exact list.

1. Download the
   [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries)
   matching your CircuitPython version.
2. From the extracted bundle's `lib/` folder, copy the following into the
   `lib/` folder on the `CIRCUITPY` drive (creating it if it doesn't exist):
   - `adafruit_bitmap_font/`
   - `adafruit_debouncer.mpy`
   - `adafruit_display_shapes/`
   - `adafruit_display_text/`
   - `adafruit_hid/`
   - `adafruit_macropad.mpy`
   - `adafruit_midi/`
   - `adafruit_pixelbuf.mpy`
   - `adafruit_simple_text_display.mpy`
   - `adafruit_ticks.mpy`
   - `neopixel.mpy`

## Installing this repository's code on the board

With CircuitPython and the libraries installed, and the board connected and
mounted as `CIRCUITPY`:

1. Clone this repository (if not already):
   ```
   git clone <this-repo-url>
   cd macropad-rp2040-macros
   ```
2. Copy the code and macros onto the device, replacing the existing files:
   ```
   cp code.py keyconfig.py /run/media/$USER/CIRCUITPY/
   cp -r macros/. /run/media/$USER/CIRCUITPY/macros/
   ```
   (Adjust the mount path if your system mounts `CIRCUITPY` elsewhere, e.g.
   `/media/$USER/CIRCUITPY` or a drive letter on Windows/macOS.)
3. CircuitPython automatically detects the file changes and restarts
   `code.py`. No reboot is required.
4. Turn the encoder dial to switch between macro apps/sets; press a key to
   run its macro.

## Adding a new macro set

Create a new file in `macros/`, e.g. `macros/MyApp.py`, following the
existing pattern in `macros/ObsTwitchStream.py`:

```python
from adafruit_hid.keycode import Keycode

app = {
    "name": "MyApp",
    "macros": [
        (0x008080, "Label", [Keycode.F13]),
        # ... up to 12 keys, plus an optional 13th entry for the encoder button
    ],
}
```

Copy the file to the device's `macros/` folder as described above; it will
be picked up automatically (files are loaded alphabetically) on the next
board reset or file save.
