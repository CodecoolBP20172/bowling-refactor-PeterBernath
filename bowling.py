def score(game):
    result = 0
    frame = 1
    first_throw = True

    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])

        if frame < 10  and get_value(game[i]) == 10:
            result += get_value(game[i+1])
            if game[i] == 'X' or game[i] == 'x':
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        if not first_throw or game[i].lower() == 'x':
            first_throw = True
            frame += 1
        else:
            first_throw = False
    return result

def get_value(char):
    if char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    elif int(char) >= 1 and int(char) <= 9:
        return int(char)
