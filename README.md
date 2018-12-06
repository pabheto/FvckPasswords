# FvckPasswords
Simple framework to generate wordlists using "classes".

# Usage
There are some types of items:
	- Characters
	- Parameters
	- Formats

Characters: Are objects with functions that return values according them.
Parameters: Store characters values.
Formats: Create a format ussing various parameters.

# Example
We want to generate a simple wordlist to guess a password like "name_birthdate"
First:
add_parameter (Don't wait args)
You choose a object between what are created, first "Name", after "Simbol" and after "Date".
After that, type:
add_format (Don't wait args)
Then, enter the 3 parameters with their alias that you choosed before.
Finally, type:
create_wordlist (Don't wait args)
Then, enter the alias of the format.
You will get a output text with all combinations between the values of the parameters without repetitions.


	

