def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    many_words = count_words(text)
    print (f"{many_words} son las veces que te voy a besar")

# Abre el archivo y guarda el contenido en una variable
def get_book_text(path):
    with open(path) as f:
        return f.read()
            
# divide el string y mide cuantas palabras son
def count_words(text):
    words = text.split()
    return len(words)

main()    