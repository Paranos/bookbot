
def main():
    with open("./books/frankenstein.txt", "r") as f : 
        text = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(countWords(text))
        print('')
        dictReader(charCounter(text))
        print("--- End report ---")
        


def countWords(text): 
    with open("/home/dzerjal/workspace/github.com/paranos/bookbot/books/frankenstein.txt", "r") as f : 
        lst = f.read().split()
        return len(lst)
        

def charCounter(text):
    alphabet = {}
    text  = text.lower()
    for char in text : 
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in alphabet.keys(): 
                alphabet[char] += 1
            else : 
                alphabet[char] = 1
    return alphabet

def dictReader(dico): 
    #trier les éléments par ordre

    #afficher les elements
    for elt in dict(sorted(dico.items(), key=lambda item: item[1], reverse=True)) : 
        print(f'The \'{elt}\' character was found {dico[elt]} times')

main()
