"""
DISCLAIMER:
This Wi-Fi Network Scanner is intended strictly for educational and ethical use only.
Do NOT use this tool to monitor unauthorized networks. Misuse is illegal.
"""

import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first Wi-Fi interface
    iface.scan()
    time.sleep(3)  # Wait for the scan to complete

    results = iface.scan_results()

    print("\nAvailable Wi-Fi Networks:\n")
    print("{:<30} | {:<15} | {:<10}".format("SSID", "BSSID", "Signal (dBm)"))
    print("-" * 65)

    for network in results:
        ssid = network.ssid
        bssid = network.bssid
        signal = network.signal
        print("{:<30} | {:<15} | {:<10}".format(ssid, bssid, signal))

if __name__ == "__main__":
    print("Scanning for Wi-Fi networks... Please wait.")
    scan_wifi()
