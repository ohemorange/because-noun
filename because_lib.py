import nltk
import re

p = re.compile('NN.*|JJ.*|VBG')

# sometimes clause, sometimes sentence
def sentence_has_because(sentence):
    tokens = nltk.word_tokenize(sentence)
    if len(tokens) <= 0:
        return False
    if tokens[-1] == ".":
        tokens = tokens[:-1]
    if len(tokens) < 2 or tokens[-2].lower() != "because":
        return False
    tagged = nltk.pos_tag(tokens) # tagged with part of speech                                                                          
    (a,b) = tagged[-1]
    if p.match(b) != None:
        return True

# takes text
# returns whether or not the text contains a
# use of prepositional because.
# this version requires that a sentence with pbc
# ends in pbc then a single permissible word.
def has_because(text):
    # ignore whitespace, use proper punctuation
    for sentence in nltk.sent_tokenize(text):
        result = sentence_has_because(sentence)
        if result == True:
            return True

    # use whitespace to mark clause end
    for sentence in text.splitlines():
        result = sentence_has_because(sentence)
        if result == True:
            return True

    return False
