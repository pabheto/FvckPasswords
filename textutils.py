from sty import fg, rs

def upper_first(word):
	nl = list(word)
	nl[0] = nl[0].upper()
	final = "".join(nl)
	return final

def clean(word):
	return word.strip().replace(" ", "")

def ki():
    print(fg.red + "KeyboardInterrupt!" + rs.all)