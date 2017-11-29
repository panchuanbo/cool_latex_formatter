import latex

def scripter(x, script='^'):
    value = ''
    for word in x.split():
        for idx, c in enumerate(word):
            c = latex.sanitize(c)
            value += str(c) if idx % 2 == 0 else (script + '{(' + str(c) + ')}')
        value += '\\text{ }'
    return value

def nester(x, script='^'):
    def wahoo(x, s):
        if len(x) == 1:
            return s + latex.sanitize(x)
        else:
            s = s + latex.sanitize(x[0]) + script + '{'
            s = wahoo(x[1:], s) + '}'
            return s

    return wahoo(x, '')
