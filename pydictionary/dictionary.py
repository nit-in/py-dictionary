#!/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
from stringcolor import *


class Dictionary:
    def __init__(self, word, max_results=5):
        self.word = word
        self.max_results = max_results
        self.color = "white"
        self.url = "https://www.dictionary.com/browse/" + str(self.word)
        self.response = requests.get(self.url).content
        self.soup = bs(self.response, "html.parser")

    def meaning(self, color):
        self.color = color
        # for the meaning part
        meanings = self.soup.find_all("div", attrs={"value": True})
        print("\nMeaning of the word:")
        meaning_list = self.soup_to_list(meanings)
        try:
            for i in range(0, self.max_results):
                meaning = self.result_string(i, meaning_list[i])
                print(cs(meaning, self.color))
        except IndexError:
            pass

    def synonyms(self, color):
        # for synonyms
        self.color = color
        print("\nsynonyms of the word:")
        synonyms_divs = self.soup.find_all("div", {"id": "synonyms"})
        for synonyms_anchors in synonyms_divs:
            synonyms_anchors = synonyms_anchors.find_all("a", class_="luna-xref")
            synonyms_list = self.soup_to_list(synonyms_anchors)
            try:
                for i in range(0, self.max_results):
                    synonym = self.result_string(i, synonyms_list[i])
                    print(cs(synonym, self.color))
            except IndexError:
                pass

    def antonyms(self, color):
        self.color = color
        print("\nantonyms of the word:")
        antonyms_divs = self.soup.find_all("div", {"id": "antonyms"})
        for antonyms_anchors in antonyms_divs:
            antonyms_anchors = antonyms_anchors.find_all("a", class_="luna-xref")
            antonyms_list = self.soup_to_list(antonyms_anchors)
            try:
                for i in range(0, self.max_results):
                    antonym = self.result_string(i, antonyms_list[i])
                    print(cs(antonym, self.color))
            except IndexError:
                pass

    def soup_to_list(self, soup_result):
        soup_list = []
        self.soup_result = soup_result
        for i in soup_result:
            soup_list.append(i.text)
        return soup_list

    def result_string(self, index, string):
        self.index = index
        self.string = string
        result = f"{int(self.index)+ 1}. {str(self.string)}"
        return result
