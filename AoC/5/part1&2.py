with open('5/input.txt') as f:
    string = f.read().strip()

# string = 'dabAcCaCBAcCcaDA'

def are_compliments(ch1, ch2):
    if ch1 == ch2:
        return False

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if ch1 in uppercase:
        return ch1.lower() == ch2
    elif ch2 in uppercase:
        return ch2.lower() == ch1

    return False

def react(string):
    i = 1
    chars = list(string)

    while i < len(chars):

        ch1 = chars[i - 1]
        ch2 = chars[i]
        
        if are_compliments(ch1, ch2):
            chars.pop(i - 1)
            chars.pop(i - 1)
            i -= 1
            
            if i < 1:
                i = 1
        else:
            i += 1

    return ''.join(chars)

def remove_then_react(ch, string):
    string = string.replace(ch, '').replace(ch.upper(), '')
    return react(string)

print(len(react(string)))

smallest = 1e9
for ch in set(string.lower()):
    reacted_length = len(remove_then_react(ch, string))

    if reacted_length < smallest:
        smallest = reacted_length

print(smallest)