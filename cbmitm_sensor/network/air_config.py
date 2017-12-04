import subprocess

class AirConfig:

	def __init__(self, interface_name):
		self.interface_name = interface_name

	def set_interface_status(self, set_up):
		process = None
		if set_up == True:
			process = subprocess.Popen(['ifconfig', self.interface_name, 'up'])
		else:
			process = subprocess.Popen(['ifconfig', self.interface_name, 'down'])
		process.wait()

	def set_monitor_mode(self, set_on):
		process = None
		if set_on == True:
			process = subprocess.Popen(['iwconfig', self.interface_name, 'mode', 'monitor'])
		else:
			process = subprocess.Popen(['iwconfig', self.interface_name, 'mode', 'managed'])
		process.wait()