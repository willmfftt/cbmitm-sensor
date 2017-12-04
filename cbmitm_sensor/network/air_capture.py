from scapy.all import *
from air_config import AirConfig

class AirCapture:

	def __init__(self, interface_name, pkt_handler):
		self.interface_name = interface_name
		self.pkt_handler = pkt_handler
		self.air_config = AirConfig(self.interface_name)

	def start(self):
		self.air_config.set_interface_status(False)
		self.air_config.set_monitor_mode(True)
		self.air_config.set_interface_status(True)

		sniff(iface=self.interface_name, prn=self.pkt_handler)
		