import because_lib
import sys

def main():
    sentences = sys.stdin.readlines()
    for sentence in sentences:
        print sentence, because_lib.has_because(sentence)

main()
