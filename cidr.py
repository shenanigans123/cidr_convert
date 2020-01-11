# Documentation

import sublime, sublime_plugin

class CidrOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 255\.255\.255\.255")
		regionstring = ""
		masks = []

		for region in ipmasks:
			regionstring = self.view.substr(region)
			regionstring = regionstring.split()
			ip = regionstring[0]
			mask = regionstring[1]
			iplen = len(ip)
			masklen = len(mask)
			regionend = region.end()
			regionstart = regionend - masklen - 1
			region = sublime.Region(regionstart, regionend)
			newregion = self.view.substr(region)

			self.view.replace(edit, region, "/32")
			#debug:
			self.view.insert(edit, self.view.size(),
				"\nDEBUG:"
				 + "\nIP: " + ip
				 + "\nMask: " + mask
				 + "\niplen: " + str(iplen)
				 + "\nmasklen: " + str(masklen)
				 + "\nregionend: " + str(regionend)
				 + "\nregionstart: " + str(regionstart)
				 + "\nnewregion: " + newregion)