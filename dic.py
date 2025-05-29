meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "SYBAU": "Una pablabrota en ingles que si alguien te lo dice es como decir: cierra tu **** boca",
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("esa palabra no esta en el diccionario")
