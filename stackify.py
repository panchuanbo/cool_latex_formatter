import utils.latex

def stack(current):
	if current == "":
		return ""
	return "\\stackrel{" + utils.latex.sanitize(current[0]) + "}{" + stack(current[1:]) + "}"

thing = raw_input("Enter your string to stackify: ")
print("$$" + stack(thing) + "$$")
