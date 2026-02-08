import usb_cdc
import usb_hid
import board
import digitalio
import storage
import time

# Pins for your Escape Key
PIN_A = board.GP6
PIN_B = board.GP0

# Get into directory
def check_button():
    # Direction 1
    out = digitalio.DigitalInOut(PIN_A)
    out.direction = digitalio.Direction.OUTPUT
    out.value = False
    in_p = digitalio.DigitalInOut(PIN_B)
    in_p.direction = digitalio.Direction.INPUT
    in_p.pull = digitalio.Pull.UP
    time.sleep(0.1)
    pressed = not in_p.value
    out.deinit()
    in_p.deinit()
    if pressed: return True

    # Direction 2
    out = digitalio.DigitalInOut(PIN_B)
    out.direction = digitalio.Direction.OUTPUT
    out.value = False
    in_p = digitalio.DigitalInOut(PIN_A)
    in_p.direction = digitalio.Direction.INPUT
    in_p.pull = digitalio.Pull.UP
    time.sleep(0.1)
    pressed = not in_p.value
    out.deinit()
    in_p.deinit()
    return pressed

if not check_button():
    storage.disable_usb_drive()

# Always enable these for communication
usb_cdc.enable(console=True, data=True)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL))
