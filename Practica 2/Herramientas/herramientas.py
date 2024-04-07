def oraciones (lista):
    """Esta funcion recibe una lista de oraciones y analiza la complijitud de las mismas en base a la cantidad de palabras"""
    cant_facil=0
    cant_aceptable=0
    cant_dificl=0
    cant_muy_dificil=0
    for aux in lista:
        cant_word=0
        phrase= aux.split(" ")
        for word in phrase:
            if not word.isnumeric():
                cant_word+=1
        if cant_word >= 0 and cant_word <=12:
            cant_facil+=1
        elif cant_word >= 13 and cant_word <= 17:
            cant_aceptable+=1
        elif cant_word >= 18 and cant_word <= 25:
            cant_dificl+=1
        elif cant_word >25:
            cant_muy_dificil+=1
    return cant_facil, cant_aceptable, cant_dificl, cant_muy_dificil

def titulo (title):
    if len(title) > 10:
        resp= False
    else:
        resp= True

