def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        file_contents= f.read()
    count_words(file_contents)
        
def count_words(content):
    word_count = {}
    char_count = {}
    words = content.split()
    
    
    for word in words:
        for char in word:
            char_count[char.lower()] = char_count.get(char.lower(),0) + 1
        word_count[word] = word_count.get(word,0) + 1
    
    print(f"{len(words)} words found in the document")    
    viewer = sorted(char_count.items(), key=lambda char:char[1],reverse=True)
    for k,v in viewer:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
        else:
            continue

main()