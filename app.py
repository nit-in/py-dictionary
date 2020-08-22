#!/bin/env python3
from pydictionary import Dictionary

print("Hello")

if __name__ == "__main__":
    while True:
        term = input("Enter the word to search:\t")
        dict = Dictionary(str(term))
        dict.meaning()
        dict.synonyms()
        dict.antonyms()
