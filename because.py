import nltk
import re

p = re.compile('NN.*|JJ.*|VBG')

# takes a sentence
# returns whether or not the sentence contains
# prepositional because.
# this version requires that it ends in pbc
# and that what follows is a single word.
def has_because(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    if tokens[-1] == ".":
        tokens = tokens[:-1]
    if len(tokens) < 2 or tokens[-2] != "because":
        return False
    tagged = nltk.pos_tag(tokens) # tagged with part of speech
    (a,b) = tagged[-1]
    return p.match(b) != None