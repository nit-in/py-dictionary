#!/bin/env python3
import requests
from bs4 import BeautifulSoup as bs


class Dictionary:
    def __init__(self, word):
        self.word = word
        self.url = "https://www.dictionary.com/browse/" + str ( self.word )
        self.response = requests.get ( self.url ).content
        self.soup = bs ( self.response, "html.parser" )
        # print(self.soup)

    def meaning(self):
        # for the meaning part
        meanings = self.soup.find_all ( "div", attrs={"value": True} )
        print ( "\nMeaning of the word:" )
        for meaning in meanings:
            print ( f"{int ( meanings.index ( meaning ) ) + 1}. {str ( meaning.text )}" )

    def synonyms(self):
        # for synonyms
        print ( "\nsynonyms of the word:" )
        synonyms_divs = self.soup.find_all ( "div", {"id": "synonyms"} )
        for synonyms_anchors in synonyms_divs:
            synonyms_anchors = synonyms_anchors.find_all ( "a", class_="luna-xref" )
            for synonyms in synonyms_anchors:
                print (
                    f"{int ( synonyms_anchors.index ( synonyms ) ) + 1}. {str ( synonyms.text )}"
                )

    def antonyms(self):
        print ( "\nantonyms of the word:" )
        antonyms_divs = self.soup.find_all ( "div", {"id": "antonyms"} )
        for antonyms_anchors in antonyms_divs:
            antonyms_anchors = antonyms_anchors.find_all ( "a", class_="luna-xref" )
            for antonyms in antonyms_anchors:
                print (
                    f"{int ( antonyms_anchors.index ( antonyms ) ) + 1}. {str ( antonyms.text )}"
                )


if __name__ == '__main__':
    while True:
        term = input ( "\nEnter a word to search:\t" )
        dict = Dictionary ( str ( term ) )
        dict.meaning ()
        dict.synonyms ()
        dict.antonyms ()
