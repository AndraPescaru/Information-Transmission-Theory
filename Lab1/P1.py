def numara_caractere(text: str) -> dict:
    
    dict= {}
    for i in range(len(text)):
        if(dict.get(text[i],0)):
            dict[text[i]] += 1
        else:
            dict[text[i]] = 1
    return dict
    
