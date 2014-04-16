# parser.py
# Erica Portnoy
# Uses the Stanford parser to parse single sentences
#
# To avoid repeated long load times, can only handle
# single sentences.
#
# Usage: spawn_stanford_parser() to load
# sentence_parse(text) - text need not end in a newline
# exit_parser() to close


import os, sys, subprocess

def feed_to_parser(text):
    p.stdin.write(text + '\nSorry.\n')

# please excuse my hardcoding.
def spawn_stanford_parser():
    sys.stdout.flush()
    global p
    p = subprocess.Popen('bash stanford-parser-full-2014-01-04/lexparser.sh -sentence newline -', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

def exit_parser():
    p.stdin.close()
    sys.stdout.flush()

# will only parse the first sentence it receives
def sentence_parse(text):
    p.stdout.flush()
    feed_to_parser(text)
    p.stdin.flush()
    p.stdout.flush()
    line = p.stdout.readline()
    out = ""
    while line != "\n":
        sys.stdout.flush()
        out += line
        line = p.stdout.readline()
    return out

def test():
    spawn_stanford_parser()
    print sentence_parse("This is a sample sentence. This is another.")
    print sentence_parse("This is a third sentence.")
    # Should print the parses of sample and third.
    exit_parser()
