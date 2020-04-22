def word_get():
    fi = open('./nlp51.txt', 'w', encoding='utf-8')
    with open('./nlp50.txt','r') as f:
        for line in f:
            word = line.replace(" ","\n")
            fi.write(word+'\n')
    f.close()
    with open('./nlp51.txt', 'r') as f:
        print(f.read())

word_get()