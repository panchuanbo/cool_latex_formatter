import latex
import supersub

x = raw_input("enter fun stuff: ")
print('$$' + supersub.nester(x, '_') + '$$')
