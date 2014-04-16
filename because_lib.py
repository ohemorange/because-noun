# call exit_because when done.

import nltk
import re
from parser import *

re_bc = re.compile('.*because.*', re.IGNORECASE)

parser_running = False

# sometimes clause, sometimes sentence
def sentence_has_because(sentence):
    global re_bc, parser_running
    # first, check if because is in there at all
    if re.search(re_bc, sentence) is None:
        return False

    # if it is, load up the parser
    if not parser_running:
        spawn_stanford_parser()
        parser_running = True

    # do fancy parsing things with the parse tree
    s_nlp_out = sentence_parse(sentence)
    tparse = nltk.tree.Tree.parse
    tree = tparse(s_nlp_out)
    print tree
    return True

    # TODO finish this method


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

# call when finished to close parser if needed
def exit_because():
    global parser_running
    if parser_running:
        exit_parser()
        parser_running = False

def test():
    s = "This is a sentence."
    t = "This is a sentence because awesome."
    print has_because(s)
    print has_because(t)
    exit_because()

test()
