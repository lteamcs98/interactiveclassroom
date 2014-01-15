from random import uniform

def cheap_magic_8_ball():
    r = uniform(0, 4)

    if r > 3:
        return "Most likely"
    elif r > 2:
        return "Ask again later"
    elif r > 1:
        return "Don't count on it"
    else:
        return "No"

print cheap_magic_8_ball()
