import latex
import supersub

val = raw_input("enter some fun strings: ")
print('$$' + supersub.scripter(val, '_') + '$$')
