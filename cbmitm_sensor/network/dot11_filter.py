from scapy.all import *

class Dot11Filter:

	def __init__(self, ssid, channel):
		self.ssid = ssid
		self.channel = channel
		self.bssid_ssid_map = {}
		self.bssid_channel_map = {}

	def pkt_match(self, pkt):
		if pkt.haslayer(Dot11):
			if pkt.type == 0 and pkt.subtype == 8:
				self.bssid_ssid_map[pkt.addr3] = pkt.info
				self.bssid_channel_map[pkt.addr3] = int(ord(pkt[Dot11Elt:3].info))

			if pkt.addr3 in self.bssid_ssid_map and pkt.addr3 in self.bssid_channel_map:
				if self.bssid_ssid_map[pkt.addr3] == self.ssid and self.bssid_channel_map[pkt.addr3] == self.channel:
					return True
		return False
