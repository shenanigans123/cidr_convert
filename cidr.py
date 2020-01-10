import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		myRegionSet = self.view.find_all("255\.255\.255\.0")
		for region in myRegionSet:
			self.view.replace(edit, region, "/24")

		self.view.insert(edit, 0, "Done")