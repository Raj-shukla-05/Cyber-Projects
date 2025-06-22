# Keylogger Implementation

## Introduction
An ethical demonstration of a keylogger built in Python using the `pynput` library. This project logs keystrokes to a file and runs in the background with a system tray icon for easy management.

## Disclaimer
```
This keylogger is developed strictly for educational and ethical purposes only.
Do NOT use this tool on any system without the owner's consent.
Misuse of this code for unauthorized access or malicious intent is illegal and punishable under law.
```

## Features
- Records keystrokes.
- Saves logs to a file (`key_log.txt`).
- Terminates on pressing 'ESC' or via system tray icon.
- Background system tray icon for management.

## Tools & Technologies
- Python 3.x
- Libraries: `pynput`, `pystray`, `PIL (Pillow)`, `threading`, `sys`, `datetime`

## How to Run
### 1. Install Dependencies
```bash
pip install pynput pystray pillow
```

### 2. Run the Keylogger
```bash
python keylogger.py
```

- Press 'ESC' to stop the keylogger.
- Or right-click the tray icon and select 'Quit'.

## Project Structure
```
Keylogger-Implementation/
│
├── keylogger.py                 # Main Python script
├── key_log.txt                  # Log file (generated on run)
├── README.md                    # Project documentation
└── Keylogger_Implementation_Report.pdf   # Final report
```

## Note
Use this tool responsibly and ethically.
