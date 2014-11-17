
import csv


class Reader:
	""" READING CSV FILE -> LIST """
	def __init__(self, filename):
		self.lst = csv.reader(open(filename), delimiter=',', quotechar='"')

	def get_list(self):
		return self.lst


