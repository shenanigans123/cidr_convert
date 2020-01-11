# Documentation

import sublime, sublime_plugin

class CidrOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):

#		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 255\.255\.255\.255")
#		regionstring = ""
#		masks = []
#
#		for region in ipmasks:
#			regionstring = self.view.substr(region)
#			regionstring = regionstring.split()
#			ip = regionstring[0]
#			mask = regionstring[1]
#			iplen = len(ip)
#			masklen = len(mask)
#			regionend = region.end()
#			regionstart = regionend - masklen - 1
#			region = sublime.Region(regionstart, regionend)
#			newregion = self.view.substr(region)
#
#			self.view.replace(edit, region, "/32")
#			#debug:
#			self.view.insert(edit, self.view.size(),
#				"\nDEBUG:"
#				 + "\nIP: " + ip
#				 + "\nMask: " + mask
#				 + "\niplen: " + str(iplen)
#				 + "\nmasklen: " + str(masklen)
#				 + "\nregionend: " + str(regionend)
#				 + "\nregionstart: " + str(regionstart)
#				 + "\nnewregion: " + newregion)

		masks = ["255.255.255.255"
			, "255.255.255.254"
			, "255.255.255.252"
		 	, "255.255.255.248"
		 	, "255.255.255.240"
		 	, "255.255.255.224"
		 	, "255.255.255.192"
		 	, "255.255.255.128"
		 	, "255.255.255.0"
		 	, "255.255.254.0"
		 	, "255.255.252.0"
		 	, "255.255.248.0"
		 	, "255.255.240.0"
		 	, "255.255.224.0"
		 	, "255.255.192.0"
		 	, "255.255.128.0"
		 	, "255.255.0.0"
		 	, "255.254.0.0"
		 	, "255.252.0.0"
		 	, "255.248.0.0"
		 	, "255.240.0.0"
		 	, "255.224.0.0"
		 	, "255.192.0.0"
		 	, "255.128.0.0"
		 	, "255.0.0.0"]

		for mask in masks:
			self.cidr_on(edit, mask)

	def cidr_on(self, edit, mask):
		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} " + mask)
		ipmasks.reverse()
		masks = []

		for region in ipmasks:
			regionstring = self.view.substr(region).split()
			regionstart = region.end() - len(regionstring[1]) - 1
			masks.append(sublime.Region(regionstart, region.end()))

		for region in masks:
			self.view.replace(edit, region, "/32")

		#debug:
#		for region in ipmasks:
#			self.view.insert(edit, self.view.size(), "\nIP: " + self.view.substr(region))
#
#		for region in masks:
#			self.view.insert(edit, self.view.size(), "\nIP: " + self.view.substr(region))

