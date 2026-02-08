# Steno-QWERTY Raspberry Pi Keyboard ⌨️

A custom mechanical keyboard project powered by the **Raspberry Pi Pico (RP2040)** and **KMK Firmware**.  
This keyboard operates as both a standard **QWERTY keyboard** and a high-speed **stenography machine**, making it suitable for everyday typing and professional steno workflows.

The firmware is Python-based using **CircuitPython + KMK**, allowing fast iteration without complex C++ toolchains.

---

## 🚀 Features

- **Dual Mode Operation**  
  Seamlessly switch between standard QWERTY typing and Steno protocols (GeminiPR / TXBolt).

- **Powered by KMK**  
  All configuration is handled in Python—no heavy compiling or flashing cycles required.

- **On-the-Fly Customization**  
  The keyboard mounts as a USB drive. Simply edit `code.py` to update layouts instantly.

- **Plover Compatible**  
  Optimized for use with the Open Steno Project’s **Plover** software for real-time shorthand input.

- **RP2040 Based**  
  Uses Raspberry Pi Pico or any RP2040-compatible controller.

---

## 🧠 Project Overview

This project bridges mechanical keyboard design with stenography input systems.  
Instead of maintaining two devices, users can type normally in QWERTY mode and instantly switch to steno mode for high-speed transcription.

KMK’s modular system enables layered keymaps and steno protocol handling without rewriting firmware.

---

## 🛠 Hardware Requirements

| Component | Description |
|---------|------------|
| Microcontroller | Raspberry Pi Pico (RP2040) or compatible board |
| Switches | Mechanical keyboard switches |
| Diodes | 1N4148 signal diodes for matrix wiring |
| PCB / Handwire | Custom PCB or hand-wired matrix |
| Interface | USB-C or Micro-USB depending on board |
| Case | Optional 3D printed or custom case |

---

## ⚡ Software Requirements

- CircuitPython  
- KMK Firmware  
- Plover (for stenography input)  

---

## 📦 Installation

### 1️⃣ Install CircuitPython

1. Download the latest CircuitPython `.UF2` for the Pico.  
2. Hold the **BOOTSEL** button while plugging in the Pico.  
3. Drag the `.uf2` file onto the `RPI-RP2` drive.  
4. The board will reboot as `CIRCUITPY`.

---

### 2️⃣ Install KMK Firmware

1. Download the KMK firmware repository.  
2. Copy the following to the root of `CIRCUITPY`:
   - `kmk/`
   - `boot.py`

---

### 3️⃣ Apply Keymap

1. Copy `code.py` from this repository to `CIRCUITPY`.  
2. Save the file.  
3. The keyboard automatically reloads with the new configuration.

---

## ⌨️ Layout Configuration

The keyboard uses a **layered system** to support both typing modes.

| Key Row | QWERTY Layer | Steno Layer |
|--------|-------------|------------|
| Top Row | Numbers / Symbols | Steno Initials |
| Home Row | A S D F … | Steno Vowels / Finals |
| Bottom Row | Modifiers | Steno Modifiers |
| Thumb Cluster | Space / Backspace | Steno Vowels |

Switching layers allows the same hardware to behave as either a normal keyboard or a steno machine.

---

## 🧩 Steno Module Setup

The firmware is configured for the **GeminiPR protocol**:

```python
from kmk.modules.steno import Steno, StenoProtocol

steno = Steno(protocol=StenoProtocol.GeminiPR)
keyboard.modules.append(steno)
