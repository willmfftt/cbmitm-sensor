from threading import Timer
from scapy.all import *

class DeauthDetector:

	def __init__(self, deauth_detected_callback, threshold=50):
		self.deauth_count = 0
		self.deauth_detected_callback = deauth_detected_callback
		self.threshold = threshold
		self.set_kill_reset_timer(False)

	def reset_deauth_count(self):
		self.deauth_count = 0
		self.set_reset_deauth_count_timer()

	def set_reset_deauth_count_timer(self):
		if self.kill_reset_timer == False:
			Timer(30, self.reset_deauth_count).start()

	def set_kill_reset_timer(self, kill_reset_timer):
		self.kill_reset_timer = kill_reset_timer
		if self.kill_reset_timer == False:
			self.set_reset_deauth_count_timer()

	def increment_deauth_count(self):
		self.deauth_count += 1
		if self.deauth_count >= self.threshold:
			self.deauth_detected_callback()

	def check_packet(self, pkt):
		if pkt.haslayer(Dot11Deauth):
			self.increment_deauth_count()