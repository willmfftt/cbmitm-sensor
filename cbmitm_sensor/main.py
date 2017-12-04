import sys
import argparse
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from network.air_capture import AirCapture
from network.dot11_filter import Dot11Filter
from detector.deauth_detector import DeauthDetector

parser = argparse.ArgumentParser(description='Sensor for detecting Channel-Based MiTM attacks')
parser.add_argument('interface', help='network interface to sniff on')
parser.add_argument('ssid', help='ssid to monitor')
parser.add_argument('channel', help='channel to monitor', type=int)

args = parser.parse_args()

def deauth_detected_callback():
	print "DEAUTH DETECTED!!!"

deauth_detector = DeauthDetector(deauth_detected_callback)
dot11_filter = Dot11Filter(args.ssid, args.channel)

def pkt_handler(pkt):
	if dot11_filter.pkt_match(pkt):
		deauth_detector.check_packet(pkt)

try:
	air_capture = AirCapture(args.interface, pkt_handler)
	air_capture.start()
except:
	deauth_detector.set_kill_reset_timer(True)
	sys.exit(-1)