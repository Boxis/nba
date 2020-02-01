def remap(entry, offset):
    if offset > 0:
        if entry < 65:
            return 65
        elif entry > 89:
            return 65
    elif offset < 0:
        if entry < 65:
            return 5
        elif entry > 89:
            return 90
    return entry

def caesar(entry, offset):
    result = ''
    for letter in entry:
        old = ord(letter)
        med = remap(old, offset)
        new = med + offset
        result += chr(new)
        print(old, med, new)
    print(entry)
    return(result)

print(caesar('ABDZ', -1))

