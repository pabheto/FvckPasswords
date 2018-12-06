#!/usr/bin/python3

from cmd import Cmd
from sty import fg, bg, ef, rs
import textutils as tu
import formats
import itertools
import os

parameters = {}
wordlist_formats = {}

class Console(Cmd):
	prompt = f"{fg.blue}(FvckPasswords){rs.all} "

	def emptyline(self):
		return

	def do_exec(self, s):
		os.system(s)

	def do_add_parameter(self, s):
		args = s.split()

		if len(args) > 0:
			print(f"{fg.red}This function don't wait args!{rs.all}")
			return

		print("Avalible parameters to add: ")
		print("----------------------------")
		for value in formats.all_parameters:
			print(value)
		print("----------------------------")
		
		try:
			pid = input("Parameter ID: ")
			alias = input("Parameter Alias: ")
		except KeyboardInterrupt:
			tu.ki()
			return

		if alias == "":
			print(f"{fg.red}You must select an alias!{rs.all}")
			return

		if pid in formats.all_parameters:
			if not alias in parameters:
				p = formats.all_parameters[pid].store_values()
				if p == None:
					return
				else:
					parameters[alias] = p
			else:
				print(f"{fg.red}Parameter already exists!{rs.all}")
		else:
			print(f"{fg.red}Parameter {pid} don't exists!{rs.all}")

		print(f"Parameter '{alias}' added succesfully!")


	def do_add_format(self, s):
		args = s.split()
		if len(args) > 0:
			print(f"{fg.red}This function don't wait args!{rs.all}")
			return

		final_parameters = []

		try:
			alias = input("Alias for the format >> ")
		except KeyboardInterrupt:
			tu.ki()
			return

		if alias in wordlist_formats:
			print(f"{fg.red}Format '{alias}' already exists!")
			return

		print("You must enter values stored in the program parameters table")
		print("You can enter multiple values in the format value1,value2,value3")

		try:
			values = input("Parameters >> ")
		except KeyboardInterrupt:
			tu.ki()
			return

		values = tu.clean(values)

		if values == "":
			print(f"{fg.red}You must enter any value!{rs.all}")
			return

		if "," in values and not values.endswith(",") :
			values = values.split(",")
			print("Format adding values: " + str(values))
			for v in values:
				if v in parameters:
					final_parameters.append(v)
				else:
					print(f"{fg.red}Parameter '{v}' not found in the parameters table!")
					return
		else:
			values.replace(",", "")
			if values in parameters:
				print("Format adding values: " + str(values))
				final_parameters.append(values)
			else:
				print(f"{fg.red}Parameter '{values}' not found in the parameters table!")
				return

		a = final_parameters
		if a == None:
			print(f"{fg.red}An error ocurred!{rs.all}")
			return
		wordlist_formats[alias] = a

		

	def do_remove_parameter(self, s):
		args = s.split()
		if len(args) == 1:
			if args[0] in parameters:
				parameters.pop(args[0])
				print(f"Parameter '{args[0]}' reemoved succesfully!")
			else:
				print(f"{fg.red}Parameter {args[0]} don't exists!{rs.all}")
		else:
			print(f"{fg.red}Usage: remove_parameter formatalias{rs.all}")

	def do_remove_format(self, s):
		args = s.split()
		if len(args) == 1:
			if args[0] in wordlist_formats:
				wordlist_formats.pop(args[0])
				print(f"Format '{args[0]}' reemoved succesfully!")
			else:
				print(f"{fg.red}Format {args[0]} don't exists!{rs.all}")
		else:
			print(f"{fg.red}Usage: remove_format formatalias{rs.all}")


	def do_create_wordlist(self, s):
		args = s.split()
		if len(args) == 0:
			print("Put the formats in format format1,format2,format3")
			try:
				output = input("Output file >> ")
			except KeyboardInterrupt:
				tu.ki()
				return

			try:
				file = open(output, "w")
			except:
				print(f"{fg.red}A problem ocurred opening the file {file}!{rs.all}")
				return

			try:
				formats_input = tu.clean(input("Formats >> "))
			except KeyboardInterrupt:
				tu.ki()
				return

			# formats_list = tu.clean(formats_input).split(",")
			formats = []
			wordlist = []

			if "," in formats_input:
				formats_input = formats_input.split(",")

				for f in formats_input:
					if f in wordlist_formats:
						formats.append(wordlist_formats[f])
					else:
						print(f"{fg.red}Format {f} don't exists in the format table! Skipping it...{rs.all}")
			else:
				if formats_input in wordlist_formats:
					formats.append(wordlist_formats[formats_input])
				else:
					print(f"{fg.red}Format {formats_input} don't exists in the format table! Skipping it...{rs.all}")

			if not len(formats) > 0:
				print(f"{fg.red}There aren't enough formats to do the wordlist!{rs.all}")
				return

			
			for f in formats:
				values = []
				for p in f:
					values.append([x for x in parameters[p]])

				print(f"{fg.cyan}Creating wordlist permutations...{rs.all}")
				permutations = list(itertools.product(*values))

				for p in permutations:
					word = "".join([x for x in p])
					if not word in wordlist:
						wordlist.append(word)

			print(f"{fg.cyan}Writting to text file...{rs.all}")

				

			file.writelines("".join([x + "\n" for x in wordlist]))
			file.close()
			print(f"{fg.cyan}Done!, saved as {file.name}{rs.all}")

		else:
			print(f"{fg.red}This function don't wait args!{rs.all}")

	def do_parameters(self, s):
		args = s.split()
		if len(args) > 0:
			print(parameters)
			print(f"{fg.red}This function don't wait args!{rs.all}")
		else:
			print("+-------------+")
			print("|  Parameters |")
			print("+-------------+")
			if not parameters:
				print(f"{fg.red}There aren't any avalible parameters!{rs.all}")
			for p in parameters:
				print(f"- {p}")

	def do_parameters_values(self, s):
		args = s.split()
		if len(args) > 0:
			print(parameters)
			print(f"{fg.red}This function don't wait args!{rs.all}")
		else:
			print("+-----------------------+")
			print("|  Parameters + Values  |")
			print("+-----------------------+")
			if not parameters:
				print(f"{fg.red}There aren't any avalible parameters!{rs.all}")
			for p in parameters:
				print(f"{fg.cyan}{p}{rs.all} => {parameters[p]}")

	def do_formats(self, s):
		args = s.split()
		if len(args) > 0:
			print(f"{fg.red}This function don't wait args!{rs.all}")

		else:
			print("+-----------+")
			print("|  Formats  |")
			print("+-----------+")
			
			str_params = []
			if not wordlist_formats:
				print(f"{fg.red}There aren't any avalible formats!{rs.all}")
			for f in wordlist_formats:
				print(f"'{f}' parameters: ")
				for p in wordlist_formats[f]:
					print(f"- {fg.cyan}{p}{rs.all}")
				print("--------------------------")

def main_menu():
	print("------------")
	print("FvckPassword")
	print("------------")

if __name__ == "__main__":
	main_menu()
	Console().cmdloop()