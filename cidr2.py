# Documentation

import sublime, sublime_plugin

class CidrOn2Command(sublime_plugin.TextCommand):

	selection = False
	ipmasks = []
	editregions = []

	def run(self, edit):

		self.masks = {
		" 255.255.255.255": "/32",
		" 255.255.255.254": "/31",
		" 255.255.255.252": "/30",
		" 255.255.255.248": "/29",
		" 255.255.255.240": "/28",
		" 255.255.255.224": "/27",
		" 255.255.255.192": "/26",
		" 255.255.255.128": "/25",
		" 255.255.255.0": "/24",
		" 255.255.254.0": "/23",
		" 255.255.252.0": "/22",
		" 255.255.248.0": "/21",
		" 255.255.240.0": "/20",
		" 255.255.224.0": "/19",
		" 255.255.192.0": "/18",
		" 255.255.128.0": "/17",
		" 255.255.0.0": "/16",
		" 255.254.0.0": "/15",
		" 255.252.0.0": "/14",
		" 255.248.0.0": "/13",
		" 255.240.0.0": "/12",
		" 255.224.0.0": "/11",
		" 255.192.0.0": "/10",
		" 255.128.0.0": "/9",
		" 255.0.0.0": "/8"
		}

		self.cidrs = {
		"/32": " 255.255.255.255",
		"/31": " 255.255.255.254",
		"/30": " 255.255.255.252",
		"/29": " 255.255.255.248",
		"/28": " 255.255.255.240",
		"/27": " 255.255.255.224",
		"/26": " 255.255.255.192",
		"/25": " 255.255.255.128",
		"/24": " 255.255.255.0",
		"/23": " 255.255.254.0",
		"/22": " 255.255.252.0",
		"/21": " 255.255.248.0",
		"/20": " 255.255.240.0",
		"/19": " 255.255.224.0",
		"/18": " 255.255.192.0",
		"/17": " 255.255.128.0",
		"/16": " 255.255.0.0",
		"/15": " 255.254.0.0",
		"/14": " 255.252.0.0",
		"/13": " 255.248.0.0",
		"/12": " 255.240.0.0",
		"/11": " 255.224.0.0",
		"/10": " 255.192.0.0",
		"/9": " 255.128.0.0",
		"/8": " 255.0.0.0"
		}

		#initialise
		self.selection = False
		self.sels = self.view.sel()
		self.ipmasks = []
		self.editregions = []



		#check if selection exists
		if self.view.sel()[0].empty():
			#Nothing selected
			self.selection = False

			#find and replace each mask in document
			for mask in self.masks:
				self.editregions = []
				match = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" + mask)
				if len(match) > 0:
					#mask matched
					for m in match:
						self.editregions.append(m)
				#inverse order
				self.editregions.reverse()
				#remove IP
				print("Searching Mask: " + str(mask))
				for region in self.editregions:
					print("  Region: " + str(region))
					print("Split: " + str(self.splitmasks(edit, region)))
					region = self.splitmasks(edit, region)
					#replace
					self.view.replace(edit, region, self.masks[mask])

		else:
			#Something selected
			self.selection = True



		#DEBUG
		print("RUN BLOCK EXECUTED")

		print("\n[selection]: ")
		print(self.selection)

		print("\n[sels]: ")
		print(self.sels)

		print("\n[ipmasks]: ")
		print(self.ipmasks)

		print("\n[editregions]: ")
		print(self.editregions)

	def replacer(self, edit, text, regions):
		#input list of regions and dictionary of text:replace
		print("REPLACER EXECUTED")

	def splitmasks(self, edit, ipmask):
		#Populate editregions
		regionstring = self.view.substr(ipmask).split()
		regionstart = ipmask.end() - len(regionstring[1]) - 1
		regionend = ipmask.end()
		newregion = sublime.Region(regionstart, regionend)
		print("SPLITMASKS returning:")
		print(newregion)
		#return mask
		return newregion