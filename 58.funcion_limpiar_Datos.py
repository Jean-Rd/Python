

#MODULO LIMPIAR DATOS////


def EliminarCaracterNoAlpha(tweet):
    return ''.join(caracter for caracter in tweet if caracter.isalpha() or caracter == ' ')

