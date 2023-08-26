from random import *

dic = {'astronomia' : ['planetas', 'estrellas', 'constelacion', 'universo', 'foton'],
        'quimica' : ['atomo', 'molecula', 'celula', 'mitocondria', 'adn'],
       'fisica' : ['energia', 'trabajo', 'esfuerzo', 'velocidad', 'aceleracion'],
       'vengadores' : ['ultron', 'wakanda', 'blackpanter', 'multiverso', 'gemas'],
       'star wars' : ['sith', 'jedi', 'fuerza', 'droide', 'clon']}


def palabra_azar(a):
    return choice(a)


def palabra_encrypt(a):
    sw = ''
    for i in range(len(a)):
        sw += '-'
    return sw


def check_position(a, b):
    return [i for i, ltr in enumerate(a) if ltr == b]


def encrypt_position(a, b, c):
    if len(a) != 0:
        s = list(b)
        for i in range(len(a)):
            s[a[i]] = c
        return "".join(s)
    else:
        return False


def juego():
    while True:
        try:
            intentos = 0
            new_ = ''
            print('\nA continuacion debe de escoger un tema de su interes\nescribiendo el numero que le corresponde')
            for i in range(len(dic.keys())):
                print(f'{i+1}. {list(dic.keys())[i]}')
            c = input('Porfavor seleccione: ')
            print(f'\nEscogiste {list(dic.keys())[int(c)-1]}\nen este tema encontraras estas palabras:')
            for i in range(len(list(dic[list(dic.keys())[int(c)-1]]))):
                print(f'{i+1}. {list(dic[list(dic.keys())[int(c)-1]])[i]}')
            ch = input('¿Deseas empezar el juego? [S/N]: ')
            if ch.lower() == 's' or ch.lower() == 'y':
                azar = palabra_azar(list(dic[list(dic.keys())[int(c)-1]]))
                encrypt = palabra_encrypt(azar)
                print('\nBienvenido al juego del ahorcado :)\nTienes que adivinar la palabra secreta\nSolo tienes 6 intentos para fallar')
                while intentos < 6:
                    print('\nTienes {} vidas'.format(6-intentos))
                    a = input('Ingresa una letra: ')
                    if not a.isdigit():
                        ck = check_position(azar, a.lower())
                        if ck:
                            if a not in new_:
                                new_ = encrypt_position(ck, encrypt, a)
                                encrypt = new_
                                print(f'\n{new_}')
                                if new_ == azar:
                                    print('\n¡Ganaste con {} vidas restantes!'.format(6-intentos))
                                    break
                                continue
                            else:
                                print('\n...Ya has acertado la letra {}'.format(a))
                        else:
                            intentos += 1
                            print('...\nLo siento, la letra "{}" no esta en la palabra secreta'.format(a))
                    else:
                        print('...\nLo siento, solo se aceptan letras')
                if intentos == 6:
                    print('\n...Perdiste\nLa palabra era: {}'.format(azar))
            else:
                continue
        except KeyboardInterrupt():
            break


juego()
