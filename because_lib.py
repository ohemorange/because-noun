# call exit_because when done.

import nltk
import re
from parser import *

re_bc = re.compile('.*because.*', re.IGNORECASE)
re_cuz = re.compile('cuz', re.IGNORECASE)

parser_running = False

# sometimes clause, sometimes sentence
def sentence_has_because(sentence):
    global re_bc, re_cuz, parser_running
    # first, check if because is in there at all
    sentence = re_cuz.sub('because', sentence)

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
    return tree_has_pbc(tree)

def is_PP_bc(tree):
    assert(tree.node == 'PP')
    word = tree[0][0].lower()
    return word == 'because' or word == 'cuz'

def tree_has_pbc(tree):
    if type(tree[-1]) == type('a_string'):
        return False
    if tree[-1].node == 'PP' and is_PP_bc(tree[-1]):
        return True
    # if the last is punctuation, the second to last can be PP
    # . matches both . and !
    if tree[-1].node == '.' and len(tree)>1 and tree[-2].node=='PP' and is_PP_bc(tree[-2]):
        return True
    for subtree in tree:
        if tree_has_pbc(subtree):
            return True
    return False


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

    # I'm worried how Stanford NLP will deal with this so
    # um let's just turn it off for now.
    if (False):
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
    print s
    print has_because(s)
    print t
    print has_because(t)
    f = open("test_sentences.txt")
    all = f.read()
    for s in all.splitlines():
        print s
        print has_because(s)
    exit_because()

test()
