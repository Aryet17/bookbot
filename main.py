def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    many_words = count_words(text)
    characters = count_characters(text)
    
    print(f"-------- Comienzo del reporte de {book_path} --------")
    print(f"\nEn total hay {many_words} palabras en el texto analizado. Distribuidas de la siguiente manera:\n")      
    
    for clave, valor in characters.items():
        print(f"La letra \'{clave}\' se repite: {valor} veces")
    
    print("\n------------Final del reporte. Te quiero <3----------")
    
# Abre el archivo y guarda el contenido en una variable
def get_book_text(path):
    with open(path) as f:
        return f.read()
            
# divide el string y mide cuantas palabras son
def count_words(content):
    words = content.split()
    return len(words)

# divide el string y cuenta cuantas palabras empizar por cada caracter
def count_characters(content):
    letras = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    for i in content.lower():
        if i in letras:
            letras[i] += 1

    return letras

main()    