import latex

def scripter(x):
    value = ''
    for word in x.split():
        for idx, c in enumerate(word):
            c = latex.sanitize(c)
            value += str(c) if idx % 2 == 0 else ('^{(' + str(c) + ')}')
        value += '\\text{ }'
    return value

val = raw_input("enter some fun strings: ")
print('$$' + scripter(val) + '$$')
