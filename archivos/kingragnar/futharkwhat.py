"""
    Futhark alphabet translation
    https://en.wikipedia.org/wiki/Elder_Futhark
"""

print("""
  ______     _   _                _               _           _
 |  ____|   | | | |              | |             | |         | |
 | |__ _   _| |_| |__   __ _ _ __| | __ __      _| |__   __ _| |_
 |  __| | | | __| '_ \ / _` | '__| |/ / \ \ /\ / / '_ \ / _` | __|
 | |  | |_| | |_| | | | (_| | |  |   <   \ V  V /| | | | (_| | |_
 |_|   \__,_|\__|_| |_|\__,_|_|  |_|\_\   \_/\_/ |_| |_|\__,_|\__|

                                        translator by @juanvelasc0
""")

diccionario={"f" : "ᚠ","u" : "ᚢ", "þ" : "ᚦ", "a" : "ᚨ", "r" : "ᚱ","c" : "ᚲ", "g" : "ᚷ", "v" : "ᚹ", "h" : "ᚺᚻ", "n" : "ᚾ", "i" : "ᛁ", "j" : "ᛃ",
"ae" : "ᛇ", "p" : "ᛈ", "z":"ᛉ","s":"ᛊᛋ", "t":"ᛏ", "b":"ᛒ", "e":"ᛖ","m":"ᛗ","l":"ᛚ","ŋ":"ᛜ ᛝ","o":"ᛟ","d":"ᛞ","_":"_","h":"ᚼ",",":",",".":".",
" ": " ","y":"y","\n":"\n"}

def encode_text(text_to_encode):
    text_to_encode = text_to_encode.lower().replace("ó","o").replace("á","a").replace("ú","u").replace("k","c").replace("y","i").replace("w","v")

    cipher_text = ""
    for letter in text_to_encode:
        for letra,valor in diccionario.items():
            if (letra == letter):
                cipher_text = cipher_text + valor
    return cipher_text

def decode_text(text_to_decode):
    decipher_text = ""
    for letter in text_to_decode:
        if(letter.rstrip() == "ᛊ"):
            decipher_text = decipher_text + "s"
        for letra,valor in diccionario.items():
            if (letter == valor):
                decipher_text = decipher_text + letra

    return decipher_text

#MAIN PROGRAM

print("\n>----------------------------------------------------------------------------------------------<\n")

print ("""Elija la opción que desee: \n\t c. Cifrado texto Castellano - Futhrak \n\t d. Descifrado texto Futhrak - Castellano \n\t a. Descifrado archivo Futhrak - Castellano""")
eleccion = input("\nOpción deseada: ")
if eleccion is "c":
    texto_sin_cifrar = input("Introduzca el texto que desea cifrar: ")
    texto_completo_coded = encode_text(texto_sin_cifrar)
    outfile = open('cifrado.txt', 'w') # Indicamos el valor 'w'.
    outfile.write(texto_completo_coded)
    print("Texto correctamente cifrado en el archivo message.txt")
    outfile.close()
elif eleccion is "d":
    texto_sin_descifrar = input("Introduzca el texto que desea descifrar: ")
    texto_completo_decode = str(decode_text(texto_sin_descifrar))
    outfile = open('descifrado.txt', 'w') # Indicamos el valor 'w'.
    outfile.write(texto_completo_decode)
    print("Texto correctamente descifrado en el archivo descifrado.txt")
    outfile.close()
elif eleccion is "a":
    archivo = input("Introduzca el nombre del archivo con extensión: ")
    infile = open(archivo, 'r')
    texto_sin_descifrar = infile.read()
    infile.close()
    texto_completo_decode = str(decode_text(texto_sin_descifrar))
    outfile = open('descifrado_archivo.txt', 'w') # Indicamos el valor 'w'.
    outfile.write(texto_completo_decode)
    print("Texto correctamente descifrado en el archivo descifrado_archivo.txt")
    outfile.close()
else:
    "No ha introducido opción valida, saliendo del programa..."
