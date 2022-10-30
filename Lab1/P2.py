def gaseste_maxim_aparitii(lista: list) -> tuple:
    dict= {}
    for i in range(len(lista)):
        if(dict.get(lista[i],0)):
            dict[lista[i]] += 1
        else:
            dict[lista[i]] = 1
   
    values = list(dict.values())

    maxim = values[0]
    for i in values:
        if(i > maxim):
            maxim = i

    keys = []
    for i in dict :
        if dict[i]==maxim :
            keys.append(i)
    
            minim = keys[0]
    for i in keys:
        if(i < minim):
            minim = i
 
    tuple = (minim , dict[minim])
    return tuple
