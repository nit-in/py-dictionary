#!/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
from stringcolor import *
import re

class Dictionary:
    def __init__(self, word, max_results=5):
        self.word = word
        self.max_results = max_results
        self.meaning_url = "https://www.dictionary.com/browse/" + str(self.word)
        self.thesaurus_url = "https://www.thesaurus.com/browse/" + str(self.word)
        self.meaning_soup = self.soup_result(self.meaning_url)
        self.thesaurus_soup = self.soup_result(self.thesaurus_url)
        self.json_data = self.thesaurus_soup.find('script', text=re.compile("searchData"))
        self.regex = re.compile(r"\"targetTerm\":\"([a-zA-Z0-9_ ]+)\"")

    def meaning(self, color="white"):
        self.color = color
        # for the meaning part
        meanings = self.meaning_soup.find_all("div", attrs={"value": True})
        print("\nMeaning of the word:")
        meaning_list = self.soup_to_list(meanings)
        try:
            for i in range(0, self.max_results):
                meaning = self.result_string(i, meaning_list[i])
                print(cs(meaning, self.color))
        except IndexError:
            pass

    def synonyms(self, color="white"):
        # for synonyms
        self.color = color
        print("\nsynonyms of the word:")
        #synonyms_divs = self.soup.find_all("div", {"id": "synonyms"})
        synonyms_data = str(self.json_data)[str(self.json_data).find("searchData"):str(self.json_data).find('"antonyms"')]
        synonyms_list = re.findall(self.regex, synonyms_data)
        try:
            for i in range(0, self.max_results):
                synonym = self.result_string(i, synonyms_list[i])
                print(cs(synonym, self.color))
        except IndexError:
            pass

    def antonyms(self, color="white"):
        self.color = color
        print("\nantonyms of the word:")
        #antonyms_divs = self.soup.find_all("div", {"id": "antonyms"})
        antonyms_data = str(self.json_data)[str(self.json_data).find('"antonyms"'):]
        antonyms_data = antonyms_data[:antonyms_data.find('"synonyms"')]
        antonyms_list = re.findall(self.regex, antonyms_data)
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
    
    def soup_result(self,url):
        self.url = url
        self.response = requests.get(self.url).content
        self.soup = bs(self.response, "lxml")
        return self.soup
