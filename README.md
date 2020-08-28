# py-dictionary
returns meaning, synonyms, antonyms for a word (scraping dictionary.com)
limit the no of results
also get meaning, synonyms and antonyms in different color

This module uses requests, bs4 and string-color modules
and scraps dictionary.com


## How to use it

## Install it
` pip install Py-Dictionary `

## Use
`from pydictionary import Dictionary`

`dict = Dictionary("fix")`

#enter the word you want to search here e.g. I used the word "fix"

`dict.meaning()`

`dict.synonyms()`

`dict.antonyms()`

This will print maximum 5 results with text having white color

If you want to increase  or decrease maximum results do this

`dic = Dictionary("fix",10)`

#now maximum 10 results will be shown

To change the color of text

`dict.meaning("red")`

`dict.synonyms("green")`

`dict.antonyms("blue")`

#To get more color look up [string-color](https://pypi.org/project/string-color/) module
or type string-color in your terminal
