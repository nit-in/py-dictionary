#!/bin/env python3
from pydictionary import Dictionary

if __name__ == "__main__":
    while True:
        term = input("\nEnter the word to search:\t")
        dict = Dictionary(str(term), max_results=5)
        dict.meaning()
        dict.synonyms()
        dict.antonyms()
