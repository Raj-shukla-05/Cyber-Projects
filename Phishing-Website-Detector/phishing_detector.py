"""
DISCLAIMER:
This tool is intended strictly for educational and ethical use only.
Do not use this tool for real-world URL filtering without further validation or machine learning enhancements.
"""

import re

# List of suspicious keywords
suspicious_keywords = [
    'verify', 'login', 'bank', 'secure', 'update',
    'confirm', 'account', 'password'
]

shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 't.co', 'ow.ly', 'is.gd']

def is_suspicious_url(url):
    reasons = []

    # Rule 1: Check for @ symbol
    if '@' in url:
        reasons.append("Contains '@' symbol")

    # Rule 2: Check for IP address
    if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url):
        reasons.append("Uses IP address instead of domain")

    # Rule 3: Check for suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            reasons.append(f"Contains keyword '{keyword}'")

    # Rule 4: Check if it uses shortening services
    for shortener in shorteners:
        if shortener in url.lower():
            reasons.append(f"Uses URL shortener '{shortener}'")

    # Rule 5: Check if too many hyphens or dots
    if url.count('-') > 5:
        reasons.append("Contains too many hyphens")
    if url.count('.') > 5:
        reasons.append("Contains too many dots")

    return reasons

if __name__ == "__main__":
    print("=== Phishing URL Detector (Rule-Based) ===")
    user_url = input("Enter a URL to check: ").strip()

    issues = is_suspicious_url(user_url)

    if issues:
        print("\n⚠️ This URL looks suspicious!\nReasons:")
        for reason in issues:
            print(f"- {reason}")
    else:
        print("\n✅ This URL appears safe based on rule-based analysis.")
