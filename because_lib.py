import nltk
import re

p = re.compile('NN.*|JJ.*|VBG')

# takes text
# returns whether or not the text contains a
# use of prepositional because.
# this version requires that a sentence with pbc
# ends in pbc then a single permissible word.
def has_because(text):
    for sentence in nltk.sent_tokenize(text):
        tokens = nltk.word_tokenize(sentence)
        if tokens[-1] == ".":
            tokens = tokens[:-1]
        if len(tokens) < 2 or tokens[-2].lower() != "because":
            continue
        tagged = nltk.pos_tag(tokens) # tagged with part of speech
        (a,b) = tagged[-1]
        if p.match(b) != None:
            return True
    return False
