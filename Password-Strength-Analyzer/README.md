# Password Strength Analyzer with Custom Wordlist Generator

## Introduction
A Python-based tool designed to:
1. Analyze password strength.
2. Generate custom wordlists for password cracking tools based on user input.

## Features
- Password strength analysis using `zxcvbn`.
- Custom wordlist generation from personal information.
- CLI-based for simplicity and quick use.

## Tools & Technologies
- Python 3.x
- Libraries: `zxcvbn`, `argparse`, `itertools`

## How to Run
### 1. Install Dependencies
```bash
pip install zxcvbn
```

### 2. Analyze a Password
```bash
python password_analyzer.py -p "YourPassword123!"
```

### 3. Generate a Custom Wordlist
```bash
python password_analyzer.py -w Name DOB PetName
# Example:
python password_analyzer.py -w Raj 18062002 Tiger
```

The generated wordlist will be saved as `wordlist.txt`.

## Project Structure
```
Password-Strength-Analyzer/
│
├── password_analyzer.py      # Main Python script
├── wordlist.txt              # Generated wordlist (sample)
├── README.md                 # Project documentation
└── Report.pdf                # Final project report
```

## Note
This tool is intended for **educational and ethical purposes only**.
