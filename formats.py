import textutils as tu
from sty import fg, rs
import itertools

class Character():
	def __init__(self):
		self.alias = ""
		self.values = []
		self.description = "Character object"

	def __str__(self):
		return self.alias

	def store_values(self):
		pass

class Name(Character):
	def store_values(self):
		self.values = []
		multiple = False

		print("Enter a name. You can enter multiple names with the format name1,name2,name3")
		try:
			name = input("Names >> ")
		except KeyboardInterrupt:
			tu.ki()
			return 

		if not name == "":
			if "," in name:
				name = tu.clean(name).split(",")
				multiple = True
			else:
				name = tu.clean(name)
				multiple = False
		else:
			print("You must select a name!")
			return 
		try:
			opc = input("Clean name format? y/n (Default = y) >> ")
		except KeyboardInterrupt:
			tu.ki()
			return


		if opc == "y" or opc == "Y" or opc == "":
			if multiple:
				for n in name:
					n = n.lower()
			else:
				name = name.lower()

			try:
				opc2 = input("Upper first letter? (Defalt = y) y/n >> ")
			except KeyboardInterrupt:
				tu.ki()
				return

			if opc2 == "y" or opc == "Y" or opc == "":
				if multiple:
					for n in name:
						self.values.append(n)
						self.values.append(tu.upper_first(n))
				else:
					self.values.append(name)
					self.values.append(tu.upper_first(name))
			elif opc2 == "n" or opc == "N":
				if multiple:
					for n in name:
						self.values.append(n)
				else:
					self.values.append(name)
			else:
				print(f"{fg.red}Option '{opc2}' is not valid!{rs.all}")
				self.store_values
		elif opc == "n" or opc == "N":
			if multiple:
				for n in name:
					self.values.append(n)
			else:
				self.values.append(name)
		else:
			print(f"{fg.red}Option '{opc}' is not valid!{rs.all}")
			return

		return self.values

class Simbol(Character):
	def store_values(self):
		self.values = []
		print("You can enter multiple simbols in the format simbol1,simbol2,simbol3")
		try:
			simbol = input("Simbol >> ")
		except KeyboardInterrupt:
			tu.ki()
			return

		if "," in simbol:
			simbol = tu.clean(simbol).split(",")
			multiple = True

		else:
			simbol = tu.clean(simbol)
			multiple = False

		if multiple:
			for n in simbol:
				self.values.append(n)
		else:
			self.values.append(simbol)

		return self.values

class Number(Character):
	def store_values(self):
		self.values = []
		try:
			number = int(input("Number >> "))
			try:
				opc = input("Inverse number? (Default = n) >> ")
			except KeyboardInterrupt:
				tu.ki()
				return

			if opc == "":
				opc = "n"
			if opc == "N" or opc == "n":
				self.values = number
			elif opc == "Y" or opc == "y":
				self.values = [number, number[::-1]]

		except KeyboardInterrupt:
			tu.ki()
			return
		except:
			print(f"{fg.red}Invalid number!{fg.red}")
			return
		return self.values

class Date(Character):
	def store_values(self):
		self.values = []
		print("Enter the date in format dd/mm/yyyy")
		try:
			date = input("Date >> ")
			if not len(date) == 8:
				print(f"{fg.red}Invalid date format!{rs.all}")
				return
		except KeyboardInterrupt:
			tu.ki()
			return
		try:
			opc = input("Date permutations? (Default = y) y/n >> ")
		except KeyboardInterrupt:
			tu.ki()
			return

		if opc == "":
			opc = "y"
		if opc == "N" or opc == "n":
			self.values = date
		elif opc == "Y" or opc == "y":
			# Date permutations
			day = date[:2]
			month = date[2:4]
			year = date[4:8]
			half_year = date[6:8]
			data = [day, month, year, half_year]
			self.values.append(year)
			self.values.append(half_year)
			perms = list(itertools.permutations(data))
			for p in perms:
				final_date = "".join([x for x in p])
				self.values.append(final_date)
		else:
			print(f"{fg.red}Option '{opc}' is not valid!{rs.all}")
			return
		return self.values

class FileRead(Character):
	def store_values(self):
		self.values = []
		try:
			path = input("File to read >> ")
		except KeyboardInterrupt:
			tu.ki()
			return

		try:
			file = open(path, "r")
		except:
			print(f"{fg.red}File can't be opened!{rs.all}")
			return

		lines = file.readlines()
		self.values.append([tu.clean(x) for x in lines if not x == ""])

		return self.values

all_parameters = {"Name" : Name(), "Simbol" : Simbol(), "Date" : Date(), "FileRead" : FileRead(), "Number" : Number()}