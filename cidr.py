# Documentation

import sublime, sublime_plugin

class CidrOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 255\.255\.255\.255")
		
		
		for region in ipmasks:
			regionstring = self.view.substr(region)
			#self.view.replace(edit, region, "/32")




















		self.view.insert(edit, 0, regionstring)