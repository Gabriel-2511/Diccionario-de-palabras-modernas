meme_dict = {
    "LOL": "una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "una ligera desaprobación",
    "CREEPY": "algo aterrador o siniestro",
    "AGGRO": "ponerse agresivo o enojado"
}

print("Hola, este es un diccionario de palabras modernas, tienes que escribir una palabra que no entiendas (en mayúsculas) y aparecerá lo que significa.")


for i in range(5):
    word = input("Escribe una palabra que no entiendas:")
    
    if word in meme_dict.keys():
        print(word, "es", meme_dict[word])
    else:
        print("No se encontró el significado de", word)
