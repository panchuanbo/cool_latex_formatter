import latex

def nester(x):
    def wahoo(x, s):
        if len(x) == 1:
            return s + latex.sanitize(x)
        else:
            s = s + latex.sanitize(x[0]) + '^{'
            s = wahoo(x[1:], s) + '}'
            return s

    return wahoo(x, '')

x = raw_input("enter fun stuff: ")
print('$$' + nester(x) + '$$')
