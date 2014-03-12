import because
import sys

def main():
    sentences = sys.stdin.readlines()
    for sentence in sentences:
        print sentence, because.has_because(sentence)

main()
