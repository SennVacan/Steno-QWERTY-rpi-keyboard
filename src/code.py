import board
import digitalio
import supervisor
import time
from kb import KMK87
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.steno import Steno
from kmk.modules.macros import Macros

# 1. SYSTEM SETTINGS
supervisor.status_bar.console = False
supervisor.runtime.autoreload = False

# 2. INITIALIZE KEYBOARD OBJECT FIRST
keyboard = KMK87()

# 3. SETUP LED HARDWARE
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# 4. DEFINE THE LED FEEDBACK CLASS
class LayerFeedback(Layers):
    last_layer = 0
    blink_until = 0

    def after_matrix_scan(self, keyboard):
        super().after_matrix_scan(keyboard)

        # Handle blink timeout
        if self.blink_until and time.monotonic() >= self.blink_until:
            led.value = False
            self.blink_until = 0

        # Layer change detection
        if keyboard.active_layers[0] != self.last_layer:
            self.last_layer = keyboard.active_layers[0]
            print(f"LAYER_CHANGE: {self.last_layer}")
            led.value = True
            self.blink_until = time.monotonic() + 0.1  # 100ms blink

# 5. ADD MODULES
keyboard.modules.append(LayerFeedback())
keyboard.modules.append(Macros())
keyboard.modules.append(Steno())
keyboard.extensions.append(MediaKeys())

# 6. KEY DEFINITIONS
MOD_L1 = KC.MO(1)
MOD_L2 = KC.MO(2)
____ = KC.TRNS
STN_TOG = KC.TG(3)

keyboard.keymap = [
    # LAYER 0: QWERTY
    [
        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        KC.TAB,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
        KC.NO,     KC.NO,   KC.LALT, KC.LCTL, MOD_L2,  KC.SPC,  KC.SPC,  MOD_L1,    ____,    KC.DEL,  KC.NO,   KC.NO
    ],
    # LAYER 1: NAV
    [
        ____, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, ____,
        ____, ____, ____, ____, ____, ____, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, ____, ____,
        ____, ____, ____, ____, ____, ____, ____, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE, ____, ____,
        KC.NO, KC.NO, ____, ____, ____, ____, ____, ____, ____, ____, KC.NO, KC.NO
    ],
    # LAYER 2: NUM/SYM
    [
        ____, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, ____,
        STN_TOG, KC.EXLM, KC.AT, KC.HASH, KC.DLR, KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, ____,
        ____, KC.EQL, KC.PLUS, KC.MINS, KC.UNDS, KC.LBRC, KC.RBRC, KC.LCBR, KC.RCBR, KC.PIPE, KC.BSLS, ____,
        KC.NO, KC.NO, ____, ____, ____, ____, ____, ____, ____, ____, KC.NO, KC.NO
    ],
    # LAYER 3: STENO
    [
        ____, KC.STN_LS1, KC.STN_LT, KC.STN_LP, KC.STN_LH, KC.STN_AS1, KC.STN_AS3, KC.STN_RF, KC.STN_RP, KC.STN_RL, KC.STN_RT, KC.STN_RD,
        ____, KC.STN_LS2, KC.STN_LK, KC.STN_LW, KC.STN_LR, KC.STN_AS2, KC.STN_AS4, KC.STN_RR, KC.STN_RB, KC.STN_RG, KC.STN_RS, KC.STN_RZ,
        ____, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.STN_A, KC.STN_O, ____, KC.STN_FN, ____, KC.NO, KC.STN_E, KC.STN_U, KC.NO, KC.NO,
    ]
]

keyboard.set_haptics = False

if __name__ == '__main__':
    keyboard.go()


