from nltk.stem import PorterStemmer

def eng_d():
    ps = PorterStemmer()
    with open('nlp51.txt','r') as f:
        for word in f:
            word = word.strip("\n")
            print(word, "\t", ps.stem(word))

eng_d()


