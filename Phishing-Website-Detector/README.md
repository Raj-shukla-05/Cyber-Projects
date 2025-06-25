# Phishing Website Detection Tool

## Introduction
A lightweight, rule-based Python tool that scans a given URL and checks for signs of phishing using heuristics. It is intended for quick and educational detection of suspicious URLs.

## Disclaimer
```
This tool is intended strictly for educational and ethical use only.
Do not use this tool for real-world URL filtering without further validation or machine learning enhancements.
```

## Features
- Checks for common phishing indicators:
  - IP addresses in URL
  - '@' symbols
  - Suspicious keywords (e.g., login, verify, update)
  - URL shortening services (bit.ly, tinyurl, etc.)
  - Excessive hyphens or dots
- Easy-to-understand CLI feedback

## Tools & Technologies
- Python 3.x
- Libraries: `re`

## How to Run

### 1. No dependencies needed (uses built-in `re` library).

### 2. Run the tool:
```bash
python phishing_detector.py
```
Then enter a URL when prompted.

## Example:
```
Enter a URL to check: https://bit.ly/secure-login

⚠️ This URL looks suspicious!
Reasons:
- Uses URL shortener 'bit.ly'
- Contains keyword 'secure'
- Contains keyword 'login'
```

## Project Structure
```
Phishing-Website-Detector/
│
├── phishing_detector.py                   # Main Python script
├── README.md                              # Project documentation
└── Phishing_Website_Detector_Report.pdf   # Final report
```

## Note
This is a basic rule-based tool. For more accurate phishing detection, ML or external threat intelligence services should be used.
