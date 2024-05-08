def find_one(list, needle):
    """
    Devuelve true si encuentra una o mas ocurrencias de needle en list
    """
    return find_n(list, needle, 1)


def find_n(list, needle, n):
    """
    Devuelve True si en la lista hay n o mas ocurrencias de needle
    False si hay menos o si n < 0
    """
    #si n >= 0 ...
    if n >= 0:
        #Inicializamos el indice y el contador
        index = 0
        count = 0

        #mientras no hayams encontrado al elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
            #si lo encontramos, actualizamos el contador
            if needle == list[index]:
                count = count + 1

            #avanzamos el siguiete elemento
            index = index + 1
        #devolvemos el resultado de comparar contador con n
        return count >= n
    else:
        return False
    

def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o mas needles seguidos
    False, para todo lo demas
    """    
    #si n >= 0
    if n >= 0:
        #inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        #mientras no haya encontrado n seguidos y la lista no se haya acabado...
        while count < n and index < len(list):
            #si lo encuentro, activo el indicador de rachas y actualizo contador
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                #si no lo encuentro, desactivo el indicador de racha y pongo a cero el contador
                streak = False
                count = 0

            #avanzo al siguiente elemento
            index = index + 1
        #devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO estemos en racha
        return count >= n and streak
    else:
        #para valores de n < 0, no tiene sentido
        return False