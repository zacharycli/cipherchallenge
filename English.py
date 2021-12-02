def is_english(test):
    for i in test:
        if i not in alpha and i != ' ' and i not in beta:
            test = test.replace(i, '')
    numerator = 0
    test = test.split(" ")
    for word in test:
        if word.lower() in words:
            numerator +=1
    return numerator/len(test)

                

def not_english(test):    
    for i in test:
        if i not in alpha and i != ' ' and i not in beta:
            test = test.replace(i, '')
    test = test.split(" ")
    noten = []
    for word in test:
        if word.lower() not in words and word not in noten:
            noten.append(word)
    print('The following words are not registered as english words. Please consider adding them to words.txt')
    for i in noten:
        print(i)

def cleanse(test):
    for i in test:
        if i not in alpha and i != ' ' and i not in beta:
            test = test.replace(i, '')
    return test

from string import ascii_lowercase as alpha
from string import ascii_uppercase as beta
try:
    from nltk.corpus import words as all_words
    words = all_words.words()
except:
    print("nltk is not operating correctly on this machine")
    print("ensure that nltk is installed on PATH")
    print("once nltk is installed, run the following commands in shell:")
    print()
    print(">>> import nltk")
    print(">>> nltk.download()")
    print()
    print("then navigate to corpus->words and download the file")
    print("if you still see this error after the fix, email me at zacharycli@crgs.co.uk")
    from time import sleep
    sleep(20)
    exit()
