SPECIAL = ['&', '%', '$', '#', '_', '{', '}']

def sanatize(x):
    x = str(x)
    if x in SPECIAL:
        return '\\' + x
    if x == '^':
        return '\\wedge'
    if x == '~':
        return '\\sim'
    if x == '\\':
        return '\\backslash'
    return x
