import sublime, sublime_plugin

class CidrOnCommand(sublime_plugin.TextCommand):

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

		#initialise variables
		global editregions
		global intersectregions
		global selection
		global sels
		global ipmasks
		selection = False
		sels = self.view.sel()
		ipmasks = []
		editregions = []
		intersectregions = []

		#check if selection exists
		if self.view.sel()[0].empty():
			#Nothing selected
			selection = False

			#find and replace each mask in document
			for mask in self.masks:
				editregions = []
				match = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" + mask)
				if len(match) > 0:
					#mask matched
					for m in match:
						editregions.append(m)
				#inverse order
				editregions.reverse()
				#remove IP portion
				for region in editregions:
					region = self.splitmasks(edit, region)
					#replace
					self.view.replace(edit, region, self.masks[mask])

		else:
			#Something selected
			selection = True

			#create set of intersections between sels and masks
			for mask in self.masks:
				editregions = []
				intersectregions = []
				match = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" + mask)
				if len(match) > 0:
					#mask matched
					for m in match:
						for sel in sels:
							if not m.intersection(sel).empty():
								intersection = m.intersection(sel)
								editregions.append(intersection)
				#inverse order
				editregions.reverse()
				#remove IP portion
				for region in editregions:
					region = self.splitmasks(edit, region)
					intersectregions.append(region)
				#replace
				for region in intersectregions:
					self.view.replace(edit, region, self.masks[mask])

	def splitmasks(self, edit, ipmask):
		#Populate editregions
		regionstring = self.view.substr(ipmask).split()
		regionstart = ipmask.end() - len(regionstring[1]) - 1
		regionend = ipmask.end()
		newregion = sublime.Region(regionstart, regionend)
		#return mask
		return newregion

class CidrOffCommand(sublime_plugin.TextCommand):

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

		#initialise variables
		global editregions
		global intersectregions
		global selection
		global sels
		global ipmasks
		selection = False
		sels = self.view.sel()
		ipmasks = []
		editregions = []
		intersectregions = []

		#check if selection exists
		if self.view.sel()[0].empty():
			#Nothing selected
			selection = False

			#find and replace each cidr in document
			for cidr in self.cidrs:
				editregions = []
				match = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" + cidr)
				if len(match) > 0:
					#cidr matched
					for m in match:
						editregions.append(m)
				#inverse order
				editregions.reverse()
				#remove IP portion
				for region in editregions:
					region = self.splitcidrs(edit, region)
					#replace
					self.view.replace(edit, region, self.cidrs[cidr])

		else:
			#Something selected
			selection = True

			#create set of intersections between sels and cidrs
			for cidr in self.cidrs:
				editregions = []
				intersectregions = []
				match = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" + cidr)
				if len(match) > 0:
					#cidr matched
					for m in match:
						for sel in sels:
							if not m.intersection(sel).empty():
								intersection = m.intersection(sel)
								editregions.append(intersection)
				#inverse order
				editregions.reverse()
				#remove IP portion
				for region in editregions:
					region = self.splitcidrs(edit, region)
					intersectregions.append(region)
				#replace
				for region in intersectregions:
					self.view.replace(edit, region, self.cidrs[cidr])

	def splitcidrs(self, edit, ipcidr):
		#Populate editregions
		regionstring = self.view.substr(ipcidr).split("/")
		regionstart = ipcidr.end() - len(regionstring[1]) - 1
		regionend = ipcidr.end()
		newregion = sublime.Region(regionstart, regionend)
		#return cidr
		return newregion