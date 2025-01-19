def read_agressive_lines():
    f = open('agression.txt', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines


def get_random_agressive_line():
    from random import choice
    lines = read_agressive_lines()
    line = choice(lines)
    line = line.strip('\n')

    return line 

def generate_random_ip():
    from random import randint 
    #return f'{randint(0,255)}.'*4[0:-1]
    return f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
