#memes
#get rekt peter
import time
import sys 
import re

inpoot = open(sys.argv[1])

Dicktionary = {}

Memecyclopedia = {}

anagrams = {}

word_list = inpoot

for word in word_list:
  Memecyclopedia["".join(sorted(word))] = word

for word in inpoot:
  word = re.sub(r'[^a-zA-Z0-9]','', word)
  if "".join(sorted(word)) in Memecyclopedia:
    anagrams[word] = Memecyclopedia["".join(sorted(word))]
